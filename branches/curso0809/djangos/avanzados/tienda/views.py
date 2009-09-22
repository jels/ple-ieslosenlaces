# Create your views here.
# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.

productos= ('Leche', 'Pan', 'Yogur', 'Vino')

def catalogo(request):
    return render_to_response('catalogo.html', {'productos':productos, 'valores':range(10)})
    
def pedido(request):
    res="Has pedido: <br/ >"
    for k, v in request.POST.items():
        if not v == "0":
            res += "%s de %s" % (v, k) + "<br />"
    return HttpResponse(res)
        