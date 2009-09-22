# -*- encoding: utf-8 -*-
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
import time


from juego.models import *

@login_required
def index(request):
    categorias = Categoria.objects.all()
    preguntas = Pregunta.objects.all()
    respuestas = Respuesta.objects.filter(usuario=request.user)
    return render_to_response('index.html', 
                                {'categorias': categorias,
                                 'preguntas': preguntas,
                                 'respuestas': respuestas,
                                 'usuario': request.user,}
                                )

@login_required
def pregunta(request, id):
    pregunta = Pregunta.objects.get(id=id)
    try:
        respuesta = Respuesta.objects.get(pregunta=id, usuario=request.user)
    except ObjectDoesNotExist:
        respuesta = None
    return render_to_response('pregunta.html', 
                                {'pregunta': pregunta,
                                 'respuesta': respuesta,
                                 'tiempo': str(int(time.time())),
                                }
                              )
@login_required
def respuesta(request):
    pregunta = Pregunta.objects.get(id=request.POST['pregunta'])
    if not request.POST.has_key('respuesta') or request.POST['respuesta'] == "":
        texto_error = "Debe elegir una opción" 
        return render_to_response('pregunta.html', 
                                {'pregunta': pregunta,
                                 'texto_error': texto_error,
                                  'tiempo': str(int(time.time())),
                                }
                              )
    else:
        opcion = request.POST['respuesta'];
        respuesta = Respuesta()
        respuesta.pregunta = pregunta
        respuesta.usuario = request.user
        respuesta.tiempo = int(time.time()) - int(request.POST['tiempo'])
        if pregunta.respuesta_correcta == opcion:
            respuesta.resultado = 1
        else:
            respuesta.resultado = 0
        respuesta.save()
        return render_to_response('respuesta.html', 
                                {'pregunta': pregunta,
                                 'respuesta': respuesta,
                                 'opcion': opcion,
                                }
                              )