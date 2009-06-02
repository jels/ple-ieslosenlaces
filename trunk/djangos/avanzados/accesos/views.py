# -*- encoding: utf-8 -*-
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

# @login_required(redirect_field_name='redirect_to')
@login_required
def vista1(request):
    c = RequestContext(request, {'usuario': request.user.username})
    return render_to_response('accesos/bienvenida.html', c)



def milogout(request):
    usuario = request.user.username
    print '*' * 10, usuario
    logout(request)
    print '*' * 10, usuario
    c = RequestContext(request, {'salida':True, 'usuario': usuario})    
    return redirect('/accesos', c)
    
def inicio(request):
    c = RequestContext(request)
    print '*' * 10, c.has_key('usuario')
    return render_to_response('accesos/inicio.html', c)

    

