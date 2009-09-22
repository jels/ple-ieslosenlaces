# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

def indice(request):
    return render_to_response('inicio.html')
    