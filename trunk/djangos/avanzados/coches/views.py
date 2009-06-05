# -*- encoding: utf-8 -*-
from models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse
from forms import *
# Create your views here.
def ajax_color_request(request):
    # Expect an auto 'type' to be passed in via Ajax and POST
    if request.is_ajax() and request.method == 'POST':
        auto_type = Coche.objects.filter(type=request.POST.get('type', ''))
        colors = auto_type.colors.all() # get all the colors for this type of auto.
    return render_to_response('eleccion.html', locals())


def url_real(request):
    return HttpResponse(u"Bienvenido a la página <strong>%s</strong>" % request.path)

def meta_info(request):
    valores = request.META.items()
    valores.sort()
    html = []
    for k, v in valores:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))