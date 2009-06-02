# -*- encoding: utf-8 -*-
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout


# @login_required(redirect_field_name='redirect_to')
@login_required
def vista1(request):
    return HttpResponse("Bienvenido")


def milogout(request):
    logout(request)
    return HttpResponse("Sesión terminada")

