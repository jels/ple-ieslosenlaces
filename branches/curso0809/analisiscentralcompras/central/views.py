# Create your views here.
import settings
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import get_template
from django.template import Template, Context
from django.contrib.auth.decorators import login_required
import time
import datetime
from central.models import *
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.tokens import default_token_generator
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.sites.models import Site, RequestSite
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext
from django.utils.http import urlquote, base36_to_int
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout
from forms import ContactForm
from django.core.mail import send_mail

secciones = ('index','catalogo','login','contacto')

def index(request):
    return render_to_response('index.html',
                              {'secciones': secciones, 
                               'actual' : 'index'})
    
def contacto(request):
    return render_to_response('contacto.html',
                              {'secciones': secciones, 
                               'actual' : 'contacto'})
    
def login(request, template_name='/templates/login.html', redirect_field_name=REDIRECT_FIELD_NAME):
    "Displays the login form and handles the login action."
    redirect_to = request.REQUEST.get(redirect_field_name, '')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Light security check -- make sure redirect_to isn't garbage.
            if not redirect_to or '//' in redirect_to or ' ' in redirect_to:
                redirect_to = settings.LOGIN_REDIRECT_URL
            from django.contrib.auth import login
            login(request, form.get_user())
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            return HttpResponseRedirect(redirect_to)
    else:
        form = AuthenticationForm(request)
    request.session.set_test_cookie()
    if Site._meta.installed:
        current_site = Site.objects.get_current()
    else:
        current_site = RequestSite(request)
    return render_to_response(template_name, {
        'form': form,
        redirect_field_name: redirect_to,
        'site_name': current_site.name,
        'secciones': secciones,
        'actual' : 'login',
        'next': request.path,
    }, context_instance=RequestContext(request))
login = never_cache(login)
    
def catalogo(request):
    productos = Producto.objects.all()
    return render_to_response('catalogo.html',
                              {'secciones': secciones, 
                               'actual' : 'catalogo', 
                               'productos' : productos})
 
@login_required   
def milogout(request):
    logout(request)
    return render_to_response('logout.html',
                              {'secciones' : secciones})
    
def alta(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = 'Peticion alta de cliente'
            almacen = form.cleaned_data['almacen']
            email = form.cleaned_data['email']
            direccion = form.cleaned_data['direccion']
            message = "Nombre Almacen: %s -- Direccion: %s -- Email: %s" % (almacen, direccion, email)
            sender = 'daienlaces@gmail.com'

            recipients = ['daienlaces@gmail.com']

            
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/central/thanks') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('alta.html', {'form': form, 
                                            'secciones': secciones})

def thanks(request):
    return render_to_response('thanks.html',
                              {'secciones' : secciones})

@login_required    
def pedido(request):
    productos = Producto.objects.all()
    contador = 0
    lista = []
    for x in range (0,10001,500):
        lista.append(x)
    if request.method == 'POST': # If the form has been submitted...
        res={}
        for k, v in request.POST.items():
            if not v == "0":
                res[Producto.objects.get(id=k).nombre] = v
            else:
                contador = contador + 1
	if len(productos) == contador:
	    return render_to_response('pedido.html',
                              {'secciones': secciones,
                               'productos':productos,
                               'lista':lista})
	else:
	    return render_to_response('muestrapedido.html',
                                  {'res':res,
                                   'secciones':secciones})
   
    return render_to_response('pedido.html',
                              {'secciones': secciones,
                               'productos':productos,
                               'lista':lista})


def lista_pedido(request):
    usuario = request.user
    ahora = datetime.datetime.now()
    res = """
    PEDIDO DE %s
    FECHA: %s - %s - %s
    %2s %-20s %20s
    """ % (usuario, ahora.day, ahora.month, ahora.year, "#", "PRODUCTO", "CANTIDAD")
    for n, (producto, cantidad) in enumerate(request.POST.items()):
        res += "%2d %-20s %20s" % (n+1,producto,cantidad)
    return res
    
@login_required    
def alta_pedido(request):
    if request.method == 'POST':
        user = request.user
        asunto = 'Nuevo documento de pedido del cliente %s' % str(user).upper()
        sender = 'daienlaces@gmail.com'
        recipients = ['daienlaces@gmail.com']
        send_mail(asunto, lista_pedido(request), sender, recipients)
        pedido = DocPedido()
        pedido.almacen = Almacen.objects.get(username=request.user.username)
        pedido.save()
        for k, v in request.POST.items():
            linea_pedido = LineaDocPedido()
            linea_pedido.docpedido = pedido
            linea_pedido.producto = Producto.objects.get(nombre=k)
            linea_pedido.cantidad = int(v)
            linea_pedido.save()

        return HttpResponseRedirect('/central/enviado_pedido') # Redirect after POST

@login_required 
def enviado_pedido(request):
    return render_to_response('enviado_pedido.html', 
                              {'secciones' : secciones})

@login_required
def historico(request):
    almacen = Almacen.objects.get(username=request.user.username)
    pedidos = DocPedido.objects.filter(almacen=almacen)
    return render_to_response('historico.html',
                              {'secciones':secciones,
                               'pedidos':pedidos})

@login_required
def detallepedido(request, np):
    pedido = DocPedido.objects.get(id=np)
    lineas = pedido.lineadocpedido_set.all()
    fecha = pedido.fecha
    if request.user.username == pedido.almacen.username:
        return render_to_response('detallepedido.html',
                                  {'np':np,
                                   'fecha':fecha,
                                   'lineas':lineas,
                                   'secciones':secciones,
                                   })
    else:
        return HttpResponseRedirect('/central/login')