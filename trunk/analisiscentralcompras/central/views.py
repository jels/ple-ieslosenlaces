# Create your views here.
import settings
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import get_template
from django.template import Template, Context
from django.contrib.auth.decorators import login_required
import time
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
    
def milogout(request):
    logout(request)
    return render_to_response('logout.html',
                              {'secciones' : secciones})
    avisos = "Usuario desconectado."
    #return HttpResponseRedirect('/index'), render_to_response('index.html',
    #                                                          {'avisos': avisos})                                            