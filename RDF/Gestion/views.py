# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.conf import settings

from RDF.Usuario.models import Usuario
from RDF.Configuracion.models import Configuracion
from RDF.Aplicacion.models import Aplicacion
from RDF.Conmutador.models import Conmutador
from RDF.Politica.models import Politica, Politica_Usuario

from .forms import formRelacion, formPolitica, formUsuario, formAplicacion, formConfiguracion, formConmutador, formLogin, formRegistro

from datetime import datetime
from passlib.apps import custom_app_context as pwd_context

import mysql.connector as mc
import wget
import os
import re

def index(request):
    applications = Aplicacion.objects.all().count()
    switches = Conmutador.objects.all().count()
    users = Usuario.objects.all().count()
    configurations = Configuracion.objects.all().count()

    context = {
        'applications' : applications,
        'switches' : switches,
        'users' : users,
        'configurations' : configurations
    }

    return render(request, 'index.html', context)

def insertar_aplicacion(request):
    if request.method == "POST":
        form = formAplicacion(request.POST, request.FILES)
        if True:
            nombre = request.POST.get("nombre")
            descripcion = request.POST.get("descripcion")
            autor = request.POST.get("autor")

            try:
                db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

            except:
                pass

            cursor = db.cursor()

            myfile = request.FILES['archivo']
            fs = FileSystemStorage()

            cursor.execute("INSERT INTO Aplicacion_aplicacion (nombre, descripcion, fecha, autor) VALUES ('" + str(nombre) + "', '" + str(descripcion) + "', CURRENT_TIMESTAMP, '" + str(autor) + "');")
            db.commit()

            filename = fs.save("App-" + str(Aplicacion.objects.latest('id').id) + ".py", myfile)
            uploaded_file_url = fs.url(filename)

            cursor.execute("UPDATE Aplicacion_aplicacion SET archivo = '" + str(uploaded_file_url) + "' WHERE id = " + str(Aplicacion.objects.latest('id').id) + ";")
            db.commit()

            cursor.close()
            db.close()            
            
            return redirect('aplicaciones')

    else:
        form = formAplicacion()

    return render(request, 'formulario_aplicacion.html', {'form':form,})

def insertar_conmutador(request):
    if request.method == "POST":
        form = formConmutador(request.POST)
        if form.is_valid():
            ip = request.POST.get("ip")
            nombre = request.POST.get("nombre")
            version = request.POST.get("version")
            controlador = request.POST.get("controlador")
            instancia = request.POST.get("instancia")
            fabricante = request.POST.get("fabricante")

            try:
                db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

            except:
                pass

            cursor = db.cursor()
            print("INSERT INTO Conmutador_conmutador(ip, nombre, version, controlador, instancia, fabricante) VALUES ('" + str(ip) + "', '" + str(nombre) + "', '" + str(version) + "', '" + str(controlador) + "', '" + str(instancia) + "', '" + str(fabricante) + "');")

            cursor.execute("INSERT INTO Conmutador_conmutador(ip, nombre, version, controlador, instancia, fabricante) VALUES ('" + str(ip) + "', '" + str(nombre) + "', '" + str(version) + "', '" + str(controlador) + "', '" + str(instancia) + "', '" + str(fabricante) + "');")
            db.commit()

            cursor.close()
            db.close()

            return redirect('conmutadores')
    else:
        form = formConmutador()

    return render(request, 'formulario_conmutador.html', {'form':form,})

def insertar_configuracion(request):
    if request.method == "POST":
        form = formConfiguracion(request.POST, request.FILES)
        if True:
            nombre = request.POST.get("nombre")
            nota = request.POST.get("nota")

            try:
                db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

            except:
                pass

            cursor = db.cursor()

            myfile = request.FILES['archivo']
            fs = FileSystemStorage()

            cursor.execute("INSERT INTO Configuracion_configuracion (nombre, nota, fecha) VALUES ('" + str(nombre) + "', '" + str(nota) + "', CURRENT_TIMESTAMP);")
            db.commit()

            filename = fs.save("Conf-" + str(Configuracion.objects.latest('id').id) + ".conf", myfile)
            uploaded_file_url = fs.url(filename)

            cursor.execute("UPDATE Configuracion_configuracion SET archivo = '" + str(uploaded_file_url) + "' WHERE id = " + str(Configuracion.objects.latest('id').id) + ";")
            db.commit()

            cursor.close()
            db.close()            
            
            return redirect('configuraciones')

    else:
        form = formConfiguracion()

    return render(request, 'formulario_configuracion.html', {'form':form,})

def insertar_relacion(request):
    if request.method == "POST":
        form = formRelacion(request.POST)
        if form.is_valid():
            politica = form.cleaned_data.get('politica')
            usuario = form.cleaned_data.get('usuario')

            try:
                db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

            except:
                pass

            cursor = db.cursor()
            cursor.execute("INSERT INTO Politica_politica_usuario (politica, usuario) VALUES (" + str(politica) + ", " + str(usuario) + " );")
            db.commit()

            cursor.close()
            db.close()

            return redirect('politicas')
    else:
        form = formRelacion()

    return render(request, 'formulario_relacion.html', {'form':form,})

def insertar_politica(request):
    switches = Conmutador.objects.order_by('id')
    if request.method == "POST":
        form = formPolitica(request.POST)
        if form.is_valid():
            porigen = form.cleaned_data.get('porigen')
            pdestino = form.cleaned_data.get('pdestino')
            accion = form.cleaned_data.get('accion')
            switch = form.cleaned_data.get('switch')

            try:
                db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

            except:
                pass

            cursor = db.cursor()
            try:
                print("INSERT INTO Politica_politica (origen, destino, accion, switch, politica) VALUES (" + str(porigen) + ", " + str(pdestino) + ", '" +str(accion) + "', '" + str(switch) + "', " + str(Politica.objects.latest('id').id + 1) + ");")
                cursor.execute("INSERT INTO Politica_politica (origen, destino, accion, switch, politica) VALUES (" + str(porigen) + ", " + str(pdestino) + ", '" +str(accion) + "', '" + str(switch) + "', " + str(Politica.objects.latest('id').id + 1) + ");")
            except:
                cursor.execute("INSERT INTO Politica_politica (origen, destino, accion, switch, politica) VALUES (" + str(porigen) + ", " + str(pdestino) + ", '" +str(accion) + "', '" + str(switch) + "', 1);")

            db.commit()

            cursor.close()
            db.close()

            return redirect('politicas')
    else:
        form = formPolitica()

    return render(request, 'formulario_politica.html', {'form':form, 'switches':switches})

def insertar_usuario(request):
    if request.method == "POST":
        form = formUsuario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            apellidos = form.cleaned_data.get('apellidos')
            correo = form.cleaned_data.get('correo')
            usuario = form.cleaned_data.get('usuario')
            credencial = form.cleaned_data.get('credencial')

            credencial = pwd_context.hash(credencial)

            try:
                db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

            except:
                pass

            cursor = db.cursor()
            cursor.execute("INSERT INTO Usuario_usuario (nombre, apellidos, correo, usuario, credencial, es_admin, ultima_sesion) VALUES ('" + str(nombre) + "', '" + str(apellidos) + "', '" + str(correo) + "', '" + str(usuario) + "', '" + str(credencial) + "', False, CURRENT_TIMESTAMP);")
            db.commit()

            cursor.close()
            db.close()

            return redirect('usuarios')
    else:
        form = formUsuario()

    return render(request, 'formulario_usuario.html', {'form':form,})

def borrar_configuracion(request, pk):

    os.system('rm media/Conf-' + str(pk) + ".conf")

    try:
        db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

    except:
        pass

    cursor = db.cursor()
    cursor.execute("DELETE FROM Configuracion_configuracion WHERE id = " + str(pk))
    db.commit()

    cursor.close()
    db.close()
    
    return redirect('configuraciones')

def borrar_conmutador(request, pk):

    try:
        db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

    except:
        pass

    cursor = db.cursor()
    cursor.execute("DELETE FROM Conmutador_conmutador WHERE id = " + str(pk))
    db.commit()

    cursor.close()
    db.close()
    
    return redirect('conmutadores')

def borrar_aplicacion(request, pk):

    os.system('rm media/App-' + str(pk) + ".py")

    try:
        db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

    except:
        pass

    cursor = db.cursor()
    cursor.execute("DELETE FROM Aplicacion_aplicacion WHERE id = " + str(pk))
    db.commit()

    cursor.close()
    db.close()
    
    return redirect('aplicaciones')

def borrar_politica(request, pk):
    try:
        db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

    except:
        pass

    cursor = db.cursor()
    cursor.execute("DELETE FROM Politica_politica WHERE id = " + str(pk))
    db.commit()

    cursor.close()
    db.close()
    
    return redirect('politicas')

def borrar_relacion(request, pk):
    try:
        db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

    except:
        pass

    cursor = db.cursor()
    cursor.execute("DELETE FROM Politica_politica_usuario WHERE id = " + str(pk))
    db.commit()

    cursor.close()
    db.close()
    
    return redirect('politicas')

def borrar_usuario(request, pk):
    try:
        db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

    except:
        pass

    cursor = db.cursor()
    cursor.execute("DELETE FROM Usuario_usuario WHERE id = " + str(pk))
    db.commit()

    cursor.close()
    db.close()
    
    return redirect('usuarios')

def admin_usuario(request, pk):
    try:
        db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

    except:
        pass

    cursor = db.cursor()
    cursor.execute("UPDATE Usuario_usuario SET es_admin = True WHERE id = " + str(pk))
    db.commit()

    cursor.close()
    db.close()
    
    return redirect('usuarios')

def mandar_mensaje(request):
    subject = "Servidor no operativo"
    message = "El servidor no responde al protocolo ICMP y el contenido en bytes devuelto por un snmpwalk es 0 \nEl servidor de respaldo ha empezado a sustituirle"
    toemail = "javier.barroso.practicas@dipucadiz.es"
    email = EmailMessage(subject, message, to=[toemail])
    email.content_subtype= 'html'
    email.send()

def existe_ping():
    response = os.system("ping -c 1 172.18.1.4")

    if response == 0:
      return True
    else:
      return False

def existe_snmpwalk():
    file = open('file.txt', 'w')
    oids = ""
    os.system('snmpwalk -v2c -c public 172.18.1.4 1.3.6.1.2.1.2.2.1.8.2 > file.txt')
    with open('file.txt', 'r') as f:
        oids = oids + "\n" + str(f.readlines())

    if oids.find("INTEGER: 1") == -1:
        return True

    else:
        return False

def rutas_respaldo(request):
    filename = wget.download('http://www.uca.es')
    os.system('mv download.wget servidor1.html')

    filename = wget.download('https://stackoverflow.com/')
    os.system('mv download.wget servidor2.html')

    #if existe_ping() and existe_snmpwalk():   
    if True and True:
        os.system('mv servidor1.html ./RDF/Gestion/Templates/servidor1.html')
        return render(request, 'servidor1.html')
    else:
        os.system('mv servidor2.html ./RDF/Gestion/Templates/servidor2.html')
        #mandar_mensaje()
        return render(request, 'servidor2.html')

def conmutadores(request):
    switches = Conmutador.objects.order_by('id')
    return render(request, 'conmutadores.html', {'switches':switches})

def aplicaciones(request):
    applications = Aplicacion.objects.order_by('id')
    return render(request, 'aplicaciones.html', {'applications':applications})

def usuarios(request):
    users = Usuario.objects.order_by('id')
    return render(request, 'usuarios.html', {'users':users})

def graficos(request):

    response = os.system("ping -c 1 172.18.1.2")

    if response != 0:
        response = os.system("ping -c 1 172.18.1.3")
        if response != 0:
            response = os.system("ping -c 1 172.18.1.3")
            if response != 0:
                response = os.system("ping -c 1 172.18.1.4")
                if response != 0:
                    return HttpResponse("No hay ninguna aplicacion en ejecucion")

    try:
        os.system('rm salida_mik')
    except:
        pass

    try:
        os.system('rm entrada_mik')
    except:
        pass

    salida_mik = open('salida_mik.txt', 'w')
    entrada_mik = open('entrada_mik.txt', 'w')

    try:
        os.system('rm salida_hp1')
    except:
        pass

    try:
        os.system('rm entrada_hp1')
    except:
        pass

    salida_hp1 = open('salida_hp1.txt', 'w')
    entrada_hp1 = open('entrada_hp1.txt', 'w')

    try:
        os.system('rm salida_hp2')
    except:
        pass

    try:
        os.system('rm entrada_hp2')
    except:
        pass

    salida_hp2 = open('salida_hp2.txt', 'w')
    entrada_hp2 = open('entrada_hp2.txt', 'w')

    os.system('snmpwalk -v2c -c public 172.18.1.4 1.3.6.1.2.1.2.2.1.10 > salida_mik.txt') 
    os.system('snmpwalk -v2c -c public 172.18.1.4 1.3.6.1.2.1.2.2.1.16 > entrada_mik.txt')
    os.system('snmpwalk -v2c -c public 172.18.1.3 1.3.6.1.2.1.2.2.1.10 > salida_hp2.txt') 
    os.system('snmpwalk -v2c -c public 172.18.1.3 1.3.6.1.2.1.2.2.1.16 > entrada_hp2.txt')
    os.system('snmpwalk -v2c -c public 172.18.1.2 1.3.6.1.2.1.2.2.1.10 > salida_hp1.txt') 
    os.system('snmpwalk -v2c -c public 172.18.1.2 1.3.6.1.2.1.2.2.1.16 > entrada_hp1.txt')

    oids_entrada = ""
    oids_salida  = ""
    with open('salida_mik.txt', 'r') as f:
        oids_salida = oids_salida + str(f.readlines())

    with open('entrada_mik.txt', 'r') as f:
        oids_entrada = oids_entrada + str(f.readlines())

    for i in range(1, 23):
        oids_entrada = str(oids_entrada).replace("iso.3.6.1.2.1.2.2.1.10." + str(i) + " = Counter32: ", "")
        oids_salida = str(oids_salida).replace("iso.3.6.1.2.1.2.2.1.16." + str(i) + " = Counter32: ", "")

    oids_entrada = re.findall(r'\b\d+\b', str(oids_entrada))
    oids_salida = re.findall(r'\b\d+\b', str(oids_salida))
    total_mikrotik_entrada = 0
    total_mikrotik_salida = 0

    for i in range(1,23):
        try:
            total_mikrotik_entrada = total_mikrotik_entrada + int(oids_entrada[i])
            total_mikrotik_salida = total_mikrotik_salida + int(oids_salida[i])
        except:
            pass

    oids_entrada = ""
    oids_salida  = ""
    with open('salida_hp2.txt', 'r') as f:
        oids_salida = oids_salida + str(f.readlines())

    with open('entrada_hp2.txt', 'r') as f:
        oids_entrada = oids_entrada + str(f.readlines())

    for i in range(1, 27):
        oids_entrada = str(oids_entrada).replace("iso.3.6.1.2.1.2.2.1.10." + str(i) + " = Counter32: ", "")
        oids_salida = str(oids_salida).replace("iso.3.6.1.2.1.2.2.1.16." + str(i) + " = Counter32: ", "")

    oids_entrada = re.findall(r'\b\d+\b', str(oids_entrada))
    oids_salida = re.findall(r'\b\d+\b', str(oids_salida))
    total_hp2_entrada = 0
    total_hp2_salida = 0

    for i in range(1,24):
        try:
            total_hp2_entrada = total_hp2_entrada + int(oids_entrada[i])
            total_hp2_salida = total_hp2_salida + int(oids_salida[i])
        except:
            pass

    oids_entrada = ""
    oids_salida  = ""
    with open('salida_hp1.txt', 'r') as f:
        oids_salida = oids_salida + str(f.readlines())

    with open('entrada_hp1.txt', 'r') as f:
        oids_entrada = oids_entrada + str(f.readlines())

    for i in range(1, 27):
        oids_entrada = str(oids_entrada).replace("iso.3.6.1.2.1.2.2.1.10." + str(i) + " = Counter32: ", "")
        oids_salida = str(oids_salida).replace("iso.3.6.1.2.1.2.2.1.16." + str(i) + " = Counter32: ", "")

    oids_entrada = re.findall(r'\b\d+\b', str(oids_entrada))
    oids_salida = re.findall(r'\b\d+\b', str(oids_salida))
    total_hp1_entrada = 0
    total_hp1_salida = 0


    for i in range(1,24):
        try:
            total_hp1_entrada = total_hp1_entrada + int(oids_entrada[i])
            total_hp1_salida = total_hp1_salida + int(oids_salida[i])
        except:
            pass
    try:
        db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

    except:
        pass

    cursor = db.cursor()

    cursor.execute("SELECT max(date_format(fecha, '%y %m %d')) as fecha FROM Grafico_grafico;")
    
    last_date = cursor.fetchone()
    last_date = [ str(x).replace(",","").replace("(u'","").replace("')","").encode("utf-8") for x in last_date ]

    if(str(last_date[0]) == str(datetime.now().strftime('%y %m %d'))):
        cursor.execute("UPDATE Grafico_grafico SET trafico = " + str(int(total_mikrotik_entrada*0.000001)) + " WHERE ip = '172.18.1.4' and tipo = 'entrada' order by fecha desc limit 1")
        cursor.execute("UPDATE Grafico_grafico SET trafico = " + str(int(total_hp1_entrada*0.000001)) + " WHERE ip = '172.18.1.2' and tipo = 'entrada' order by fecha desc limit 1")
        cursor.execute("UPDATE Grafico_grafico SET trafico = " + str(int(total_hp2_entrada*0.000001)) + " WHERE ip = '172.18.1.3' and tipo = 'entrada' order by fecha desc limit 1")
        cursor.execute("UPDATE Grafico_grafico SET trafico = " + str(int(total_mikrotik_salida*0.000001)) + " WHERE ip = '172.18.1.4' and tipo = 'salida' order by fecha desc limit 1")
        cursor.execute("UPDATE Grafico_grafico SET trafico = " + str(int(total_hp1_salida*0.000001)) + " WHERE ip = '172.18.1.2' and tipo = 'salida' order by fecha desc limit 1")
        cursor.execute("UPDATE Grafico_grafico SET trafico = " + str(int(total_hp2_salida*0.000001)) + " WHERE ip = '172.18.1.3' and tipo = 'salida' order by fecha desc limit 1")
    else:
        cursor.execute("INSERT INTO Grafico_grafico (fecha, ip, trafico, tipo) VALUES (CURRENT_TIMESTAMP, '172.18.1.4', " + str(int(total_mikrotik_entrada*0.000001)) + ", 'entrada')") # MegaBytes
        cursor.execute("INSERT INTO Grafico_grafico (fecha, ip, trafico, tipo) VALUES (CURRENT_TIMESTAMP, '172.18.1.4', " + str(int(total_mikrotik_salida*0.000001)) + ", 'salida')")
        cursor.execute("INSERT INTO Grafico_grafico (fecha, ip, trafico, tipo) VALUES (CURRENT_TIMESTAMP, '172.18.1.3', " + str(int(total_hp2_entrada*0.000001)) + ", 'entrada')") # MegaBytes
        cursor.execute("INSERT INTO Grafico_grafico (fecha, ip, trafico, tipo) VALUES (CURRENT_TIMESTAMP, '172.18.1.3', " + str(int(total_hp2_salida*0.000001)) + ", 'salida')")
        cursor.execute("INSERT INTO Grafico_grafico (fecha, ip, trafico, tipo) VALUES (CURRENT_TIMESTAMP, '172.18.1.2', " + str(int(total_hp1_entrada*0.000001)) + ", 'entrada')") # MegaBytes
        cursor.execute("INSERT INTO Grafico_grafico (fecha, ip, trafico, tipo) VALUES (CURRENT_TIMESTAMP, '172.18.1.2', " + str(int(total_hp1_salida*0.000001)) + ", 'salida')")

    db.commit()

    # -------------------------------------------------------------------------------------- TRAFICO -----------------------------------------------------

    cursor.execute("SELECT trafico FROM Grafico_grafico WHERE fecha = any (SELECT max(fecha) FROM Grafico_grafico) ORDER BY ip;")

    data_trafico = cursor.fetchall()
    data_trafico = [ int(str(x).replace(",","").replace("(","").replace(")","")) for x in data_trafico ]

    cursor.execute("SELECT ip FROM Grafico_grafico WHERE fecha = any (SELECT max(fecha) FROM Grafico_grafico) ORDER BY ip") # Entrada + Salida

    labels_idps = cursor.fetchall()
    labels_idps = [ str(x).replace(",","").replace("(u'","").replace("')","").encode("utf-8") for x in labels_idps ]

    i = 0
    for x in labels_idps:
        if i%2==0:
            labels_idps[i] = labels_idps[i] + " Entrada"
        else:
            labels_idps[i] = labels_idps[i] + " Salida"
        i = i + 1

    labels_idps = [ str(x).replace(",","").replace("(u'","").replace("')","").encode("utf-8") for x in labels_idps ]

    cursor.execute("SELECT max(trafico) FROM Grafico_grafico")

    max_trafico = cursor.fetchone()
    max_trafico = int(str(max_trafico[0]))

    # -------------------------------------------------------------------------------------- RENDIMIENTO ---------------------------------------------------------------------------------

    data_rendimiento = []

    i = 0
    for x in data_trafico:
        if i%2==0:
            try:
                data_rendimiento.append(data_trafico[i] + data_trafico[i+1])
            except:
                pass
        else:
            pass
        i = i + 1

    labels_rendimiento = []

    i = 0
    for x in labels_idps:
        if i%2==0:
            labels_rendimiento.append(str(labels_idps[i]).replace(" Entrada", "").replace("u", "").encode("utf-8"))
        else:
            pass
        i = i + 1

    labels_rendimiento = [ str(x).replace(",","").replace("(u'","").replace("')","").encode("utf-8") for x in labels_rendimiento ]

    # -------------------------------------------------------------------------------------- ACTIVIDAD ---------------------------------------------------------------------------------            

    cursor.execute("SELECT trafico FROM Grafico_grafico WHERE ip = '172.18.1.4' ORDER BY id desc;")

    data_actividad = cursor.fetchall()
    data_actividad = [ int(str(x).replace(",","").replace("(","").replace(")","")) for x in data_actividad ]

    data_actividad4 = []

    i = 0
    for x in data_actividad:
        if i%2==0:
            try:
                data_actividad4.append(data_actividad[i] + data_actividad[i+1])
            except:
                pass
        else:
            pass
        i = i + 1

    cursor.execute("SELECT distinct date_format(fecha, '%d %b') as fecha FROM Grafico_grafico WHERE ip = '172.18.1.4' ORDER BY fecha asc;")

    labels_actividad4 = cursor.fetchall()
    labels_actividad4 = [ str(x).replace(",","").replace("(u'","").replace("')","").encode("utf-8") for x in labels_actividad4 ]


    cursor.execute("SELECT trafico FROM Grafico_grafico WHERE ip = '172.18.1.3' ORDER BY id desc;")

    data_actividad = cursor.fetchall()
    data_actividad = [ int(str(x).replace(",","").replace("(","").replace(")","")) for x in data_actividad ]

    data_actividad3 = []

    i = 0
    for x in data_actividad:
        if i%2==0:
            try:
                data_actividad3.append(data_actividad[i] + data_actividad[i+1])
            except:
                pass
        else:
            pass
        i = i + 1

    cursor.execute("SELECT distinct date_format(fecha, '%d %b') as fecha FROM Grafico_grafico WHERE ip = '172.18.1.3' ORDER BY fecha asc;")

    labels_actividad3 = cursor.fetchall()
    labels_actividad3 = [ str(x).replace(",","").replace("(u'","").replace("')","").encode("utf-8") for x in labels_actividad3 ]


    cursor.execute("SELECT trafico FROM Grafico_grafico WHERE ip = '172.18.1.2' ORDER BY id desc;")

    data_actividad = cursor.fetchall()
    data_actividad = [ int(str(x).replace(",","").replace("(","").replace(")","")) for x in data_actividad ]

    print(str(data_actividad))
    data_actividad2 = []

    i = 0
    for x in data_actividad:
        if i%2==0:
            try:
                data_actividad2.append(data_actividad[i] + data_actividad[i+1])
            except:
                pass
        else:
            pass
        i = i + 1

    print(str(data_actividad2))

    cursor.execute("SELECT distinct date_format(fecha, '%d %b') as fecha FROM Grafico_grafico WHERE ip = '172.18.1.2' ORDER BY fecha asc;")

    labels_actividad2 = cursor.fetchall()
    labels_actividad2 = [ str(x).replace(",","").replace("(u'","").replace("')","").encode("utf-8") for x in labels_actividad2 ]

    print(str(labels_actividad2))
    cursor.close()
    db.close()

    return render(request, 'graficos.html', {'labels_idps':str(labels_idps), 'data_trafico':data_trafico, 'max_trafico':max_trafico, 'labels_rendimiento':labels_rendimiento, 'data_rendimiento':data_rendimiento, 'labels_actividad2':labels_actividad2, 'data_actividad2':data_actividad2, 'labels_actividad3':labels_actividad3, 'data_actividad3':data_actividad3, 'labels_actividad4':labels_actividad4, 'data_actividad4':data_actividad4})

def login(request):
    if request.method == "POST":
        form = formLogin(request.POST)
        if True:
            usuario = request.POST.get("usuario")
            credencial = request.POST.get("credencial")

            try:
                db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

            except:
                pass

            cursor = db.cursor()
            cursor.execute("SELECT credencial FROM Usuario_usuario WHERE es_admin = 1 and usuario = '" + str(usuario) + "'")
            password = cursor.fetchone()
            try:
                password = [ str(x).replace(",","").replace("(u'","").replace("')","").encode("utf-8") for x in password ]
                if pwd_context.verify(credencial, password[0]) == True:
                    cursor.execute("UPDATE Usuario_usuario SET ultima_sesion = CURRENT_TIMESTAMP WHERE usuario = '" + str(usuario) + "'")
                    db.commit()
                    return redirect('index')
            except:
                pass

    else:
        form = formLogin()

    return render(request, 'login.html')

def registro(request):
    if request.method == "POST":
        form = formRegistro(request.POST)
        if True:
            nombre = request.POST.get('nombre')
            apellidos = request.POST.get('apellidos')
            correo = request.POST.get('correo')
            usuario = request.POST.get('usuario')
            credencial = request.POST.get('credencial')
            credencial2 = request.POST.get('credencial2')

            print("cr1: " + str(credencial))
            print("cr2: " + str(credencial2))

            if str(credencial) == str(credencial2):

                credencial = pwd_context.hash(credencial)

                try:
                    db = mc.connect (host = "localhost", user = "root", passwd = "root", db = "rdr")

                except:
                    pass

                cursor = db.cursor()
                cursor.execute("INSERT INTO Usuario_usuario (nombre, apellidos, correo, usuario, credencial, es_admin, ultima_sesion) VALUES ('" + str(nombre) + "', '" + str(apellidos) + "', '" + str(correo) + "', '" + str(usuario) + "', '" + str(credencial) + "', False, CURRENT_TIMESTAMP);")
                db.commit()

                cursor.close()
                db.close()

                return HttpResponse("Registro completado. Espere a que el administrador confirme su alta en el sistema.")

            else:
                return HttpResponse("Ambas contraseñas no coinciden.")
    else:
        print("request method no es POST")
        form = formRegistro()

    return render(request, 'register.html')

def topologia(request):
    response = os.system("ping -c 1 172.22.9.89")

    if response == 0:
      return redirect("http://172.22.9.89:8080/")
    else:
      return HttpResponse("No hay ninguna aplicacion en ejecucion")        

def nuevas_configuraciones(request):
    return insertar_configuracion(request)

def nuevas_aplicaciones(request):
    return insertar_aplicacion(request)

def nuevas_politicas(request):
    return insertar_politica(request)

def nuevas_relaciones(request):
    return insertar_relacion(request)

def nuevos_usuarios(request):
    return insertar_usuario(request)

def nuevos_conmutadores(request):
    return insertar_conmutador(request)

def politicas(request):
    policies = Politica.objects.order_by('id')
    policies_users = Politica_Usuario.objects.order_by('id');
    return render(request, 'politicas.html', {'policies':policies, 'policies_users':policies_users})

def configuraciones(request):
    configurations = Configuracion.objects.order_by('id')
    return render(request, 'configuraciones.html', {'configurations':configurations})
