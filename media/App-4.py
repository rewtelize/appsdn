# Copyright (C) 2011 Nippon Telegraph and Telephone Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
An OpenFlow 1.0 L2 learning switch implementation.
"""


from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, HANDSHAKE_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.mac import haddr_to_bin
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
import sys

from ryu.lib.packet import packet, ethernet, arp, ipv4
import array

from ryu.lib import stplib
from ryu.lib import dpid as dpid_lib

import mysql.connector as mc

class SimpleSwitch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]
    _CONTEXTS = {'stplib': stplib.Stp}
    try:
        db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

    except:
        pass

    cursor = db.cursor()
    cursor.execute("SELECT origen, destino FROM Politica_politica WHERE accion = 'Rechazar' and switch = '" + str("127.0.0.1") +"';")
    denied_ports_local = cursor.fetchall()

    cursor.execute("SELECT origen, destino FROM Politica_politica WHERE accion = 'Rechazar' and switch = '" + str("172.18.1.2") +"';")
    denied_ports_hp1 = cursor.fetchall()

    cursor.execute("SELECT origen, destino FROM Politica_politica WHERE accion = 'Rechazar' and switch = '" + str("172.18.1.3") +"';")
    denied_ports_hp2 = cursor.fetchall()

    cursor.execute("SELECT origen, destino FROM Politica_politica WHERE accion = 'Rechazar' and switch = '" + str("172.18.1.4") +"';")
    denied_ports_mik = cursor.fetchall()

    cursor.execute("SELECT origen, destino FROM Politica_politica WHERE accion = 'Aceptar' and switch = '" + str("127.0.0.1") +"';")
    accepted_ports_local = cursor.fetchall()

    cursor.execute("SELECT origen, destino FROM Politica_politica WHERE accion = 'Aceptar' and switch = '" + str("172.18.1.2") +"';")
    accepted_ports_hp1 = cursor.fetchall()

    cursor.execute("SELECT origen, destino FROM Politica_politica WHERE accion = 'Aceptar' and switch = '" + str("172.18.1.3") +"';")
    accepted_ports_hp2 = cursor.fetchall()

    cursor.execute("SELECT origen, destino FROM Politica_politica WHERE accion = 'Aceptar' and switch = '" + str("172.18.1.4") +"';")
    accepted_ports_mik = cursor.fetchall()

    cursor.close()
    db.close()

    print("[DEDALO] Inicio aplicacion SimpleSwitch")

    def __init__(self, *args, **kwargs):
        super(SimpleSwitch, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        self.stp = kwargs['stplib']

        # Sample of stplib config.
        #  please refer to stplib.Stp.set_config() for details.
        '''
        config = {
                  dpid_lib.str_to_dpid('100070106f397300'):
                    {'bridge': {'priority': 0x8000}},
                  dpid_lib.str_to_dpid('100070106f3932c0'):
                    {'bridge': {'priority': 0xa000}},
                    dpid_lib.str_to_dpid('000364d154f8ba3a'):
                    {'bridge': {'priority': 0x9000}}}
        self.stp.set_config(config)
        '''

    def add_flow(self, datapath, in_port, dst, src, actions):
        print("[DEDALO] Nuevo flujo")
        ofproto = datapath.ofproto

        match = datapath.ofproto_parser.OFPMatch(
            in_port=in_port,
            dl_dst=haddr_to_bin(dst), dl_src=haddr_to_bin(src))

        mod = datapath.ofproto_parser.OFPFlowMod(
            datapath=datapath, match=match, cookie=0,
            command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
            priority=ofproto.OFP_DEFAULT_PRIORITY,
            flags=ofproto.OFPFF_SEND_FLOW_REM, actions=actions)
        datapath.send_msg(mod)

    def delete_flow(self, datapath):
        print("[DEDALO] Eliminacion de flujo")
        ofproto = datapath.ofproto

        wildcards = ofproto_v1_0.OFPFW_ALL
        match = datapath.ofproto_parser.OFPMatch(
            wildcards, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        mod = datapath.ofproto_parser.OFPFlowMod(
            datapath=datapath, match=match, cookie=0,
            command=ofproto.OFPFC_DELETE)
        datapath.send_msg(mod)


    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):

        try:
            pkt = packet.Packet(array.array('B', ev.msg.data))
            eth_pkt = pkt.get_protocol(ethernet.ethernet)
            arp_pkt = pkt.get_protocol(arp.arp)
            ipv4_pkt = pkt.get_protocol(ipv4.ipv4)

            if arp_pkt:
                pak = arp_pkt
            elif ipv4_pkt:
                pak = ipv4_pkt
            else:
                pak = eth_pkt
        except:
            pass

        #self.logger.info("[DEDALO] pkt: " + str(pkt) + " eth_pkt: " + str(eth_pkt) + " ipv4_pkt: " + str(ipv4_pkt) + " arp_pkt: " + str(arp_pkt))

        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto

        self.logger.info("[DEDALO] Direccion: " + str(datapath.address))
        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocol(ethernet.ethernet)

        if eth.ethertype == ether_types.ETH_TYPE_LLDP:
            # ignore lldp packet
            return

        dst = eth.dst
        src = eth.src

        dpid = datapath.id
        self.mac_to_port.setdefault(dpid, {})

        # learn a mac address to avoid FLOOD next time
        self.mac_to_port[dpid][src] = msg.in_port

        if dst in self.mac_to_port[dpid]:
            out_port = self.mac_to_port[dpid][dst]
        else:
            out_port = ofproto.OFPP_FLOOD

        actions = [datapath.ofproto_parser.OFPActionOutput(out_port)]

        address = str(datapath.address).split(",")
        address = address[0].replace("(", "").replace("'", "")

        if(address == "172.18.1.2"):
            denied_ports = self.denied_ports_hp1
            accepted_ports = self.accepted_ports_hp1

        if(address == "172.18.1.3"):
            denied_ports = self.denied_ports_hp2
            accepted_ports = self.accepted_ports_hp2

        if(address == "172.18.1.4"):
            denied_ports = self.denied_ports_mik
            accepted_ports = self.accepted_ports_mik

        tupla = "(" + str(msg.in_port) + ", " + str(out_port) + ")"

        if tupla not in str(denied_ports) or tupla in str(accepted_ports):
            if out_port != ofproto.OFPP_FLOOD:
                self.add_flow(datapath, msg.in_port, dst, src, actions)

        data = None
        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data

        print("[DEDALO] Paquete entrante en dispositivo " + str(dpid) + " mac origen " + str(src) + " mac destino " + str(dst))
        print("[DEDALO] Puerto de entrada " + str(msg.in_port) + " y puerto de salida " + str(out_port))

        tupla = "(" + str(msg.in_port) + ", " + str(out_port) + ")"
        if tupla not in str(denied_ports) or tupla in str(accepted_ports):
            out = datapath.ofproto_parser.OFPPacketOut(
                datapath=datapath, buffer_id=msg.buffer_id, in_port=msg.in_port,
                actions=actions, data=data)

            datapath.send_msg(out)
            print("[DEDALO] Tabla CAM: " + str(self.mac_to_port) + "\n")

    @set_ev_cls(stplib.EventTopologyChange, MAIN_DISPATCHER)
    def _topology_change_handler(self, ev):
        dp = ev.dp
        dpid_str = dpid_lib.dpid_to_str(dp.id)
        print("[DEDALO][Topologia][dpid=" + str(dpid_str) + "] Vaciado de TCAM")

        if dp.id in self.mac_to_port:
            del self.mac_to_port[dp.id]
        self.delete_flow(dp)

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def _erase_flows_table(self, ev):
        print("[DEDALO] Tablas de flujos reseteadas")
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto

        wildcards = ofproto_v1_0.OFPFW_ALL
        match = datapath.ofproto_parser.OFPMatch(
            wildcards, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        mod = datapath.ofproto_parser.OFPFlowMod(
            datapath=datapath, match=match, cookie=0,
            command=ofproto.OFPFC_DELETE)
        datapath.send_msg(mod)

    @set_ev_cls(stplib.EventPortStateChange, MAIN_DISPATCHER)
    def _port_state_change_handler(self, ev):
        dpid_str = dpid_lib.dpid_to_str(ev.dp.id)
        of_state = {stplib.PORT_STATE_DISABLE: 'DISABLE',
                    stplib.PORT_STATE_BLOCK: 'BLOCK',
                    stplib.PORT_STATE_LISTEN: 'LISTEN',
                    stplib.PORT_STATE_LEARN: 'LEARN',
                    stplib.PORT_STATE_FORWARD: 'FORWARD'}
        self.logger.debug("[dpid=%s][port=%d] state=%s",
            dpid_str, ev.port_no, of_state[ev.port_state])

    @set_ev_cls(ofp_event.EventOFPPortStatus, MAIN_DISPATCHER)
    def _port_status_handler(self, ev):
        msg = ev.msg
        reason = msg.reason
        port_no = msg.desc.port_no

        ofproto = msg.datapath.ofproto
        if reason == ofproto.OFPPR_ADD:
            self.logger.info("port added %s", port_no)
        elif reason == ofproto.OFPPR_DELETE:
            self.logger.info("port deleted %s", port_no)
        elif reason == ofproto.OFPPR_MODIFY:
            self.logger.info("port modified %s", port_no)
        else:
            self.logger.info("Illeagal port state %s %s", port_no, reason)
