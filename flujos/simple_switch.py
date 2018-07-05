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
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.mac import haddr_to_bin
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
import sys

from ryu.lib.packet import packet, ethernet, arp, ipv4
import array

class SimpleSwitch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]
    print("[DEDALO] Inicio aplicacion SimpleSwitch")

    def __init__(self, *args, **kwargs):
        super(SimpleSwitch, self).__init__(*args, **kwargs)
        self.mac_to_port = {}

    def add_flow(self, datapath, in_port, dst, src, actions):
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


    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):

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

        dpid2 = dpid
        src2 = src
        dst2 = dst

        if dpid2 == 967640817955584:
             dpid2 = 'Switch HP-2'
        if dpid2 == 1249115794649792:
             dpid2 = 'Switch HP-1'
        if src2 == '74:da:da:33:eb:23':
             src2 = 'Portatil Manolo'
        if src2 == '00:1f:29:5f:7b:98':
             src2 = 'Servidor Controlador'
        if dst2 == '74:da:da:33:eb:23':
             dst2 = 'Portatil Manolo'

        # learn a mac address to avoid FLOOD next time
        #self.mac_to_port[1249115794649792][str('70:10:6f:39:73:00')] = 24
        #self.mac_to_port[967640817955584][str('00:1f:29:5f:7b:98')] = 24
        self.mac_to_port[dpid][src] = msg.in_port

        if dst in self.mac_to_port[dpid]:
            out_port = self.mac_to_port[dpid][dst]
        else:
            out_port = ofproto.OFPP_FLOOD

        #if out_port == 2 or out_port == 4:
        #    out_port = 0
        actions = [datapath.ofproto_parser.OFPActionOutput(out_port)]

        # install a flow to avoid packet_in next time
        if out_port != ofproto.OFPP_FLOOD:
            print("[DEDALO] Flujo instalado")
            self.add_flow(datapath, msg.in_port, dst, src, actions)

        data = None
        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data

        print("[DEDALO] Paquete entrante en dispositivo " + str(dpid2) + " mac origen " + str(src2) + " mac destino " + str(dst2))
        print("[DEDALO] Puerto de entrada " + str(msg.in_port) + " y puerto de salida " + str(out_port))

        out = datapath.ofproto_parser.OFPPacketOut(
            datapath=datapath, buffer_id=msg.buffer_id, in_port=msg.in_port,
            actions=actions, data=data)

        datapath.send_msg(out)
        print("[DEDALO] Tabla CAM: " + str(self.mac_to_port) + "\n")

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
