# -*- encoding: utf-8 -*-
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.template import RequestContext

# @login_required(redirect_field_name='redirect_to')
@login_required
def vista1(request):
    c = RequestContext(request, {'usuario': request.user.username})
    return render_to_response('accesos/bienvenida.html', c)



def milogout(request):
    logout(request)
    return HttpResponse("Sesión terminada")

