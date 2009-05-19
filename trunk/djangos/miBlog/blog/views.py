# Create your views here.
# -*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template  # para cargar el template
import datetime
from django.shortcuts import render_to_response

modelo = u"""
<html>
<head><title>Página de prueba</title></head>
<body>
<h1>Página de prueba</h1>
<p>%s</p>
</body>
</html>
"""
def hola(request):
    return HttpResponse(modelo % u"Hola, buenos días")

def hora(request):
    return HttpResponse(modelo % datetime.datetime.now())

# forma mala
def hora_menos_uno(request):
    return HttpResponse(modelo % (datetime.datetime.now()-datetime.timedelta(hours=1)))

def hora_mas(request, h):
    return HttpResponse(modelo % (datetime.datetime.now()+
                                  datetime.timedelta(hours=int(h))))

def hora_mas_t(request, h):
    t = get_template('hora.html')
    c = Context({'hora': datetime.datetime.now()+
                 datetime.timedelta(hours=int(h))})
    return HttpResponse(t.render(c))
    
def lista_empleados(request):
    conexion='dai1/tiger@ENLACES5'
    import cx_Oracle
    c = cx_Oracle.connect(conexion)
    cursor = c.cursor()
    empleados = "select * from emp"
    cursor.execute(empleados)
    lempleados = cursor.fetchall()
    
    return render_to_response('empleados2.html',{'empleados': lempleados} )
    
    

    



