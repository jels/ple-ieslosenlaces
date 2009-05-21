# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

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