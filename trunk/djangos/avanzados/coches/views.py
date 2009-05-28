from models import *
from django.shortcuts import render_to_response
# Create your views here.
def ajax_color_request(request):
    # Expect an auto 'type' to be passed in via Ajax and POST
    if request.is_ajax() and request.method == 'POST':
        auto_type = Coche.objects.filter(type=request.POST.get('type', ''))
        colors = auto_type.colors.all() # get all the colors for this type of auto.
    return render_to_response('eleccion.html', locals())

