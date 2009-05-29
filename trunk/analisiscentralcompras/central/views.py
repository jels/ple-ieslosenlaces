# Create your views here.
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import get_template
from django.template import Template, Context
import time
from central.models import *


def index(request):
    secciones = ('index','catalogo','login','contacto')
    return render_to_response('index.html',
                              {'secciones': secciones, 'actual' : 'index'})
    