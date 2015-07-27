# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.

login_var = '/login/'

def index(request):
    return render(request, 'ibsadmin/index.html')

def applogin(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/resumen/')
    loginForm = login_form()
    return render_to_response('ibsadmin/login.html',{'login_form': loginForm,'user': request.user},context_instance=RequestContext(request))

def login_process(request):
    print('test')
    if not request.user.is_anonymous():
        messages.success(request, '¡Bienvenido!')
        return HttpResponseRedirect('/resumen/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # redireccionar al inicio
                messages.success(request, '¡Bienvenido!')
                return HttpResponseRedirect('/resumen/')
            else:
                # Mensaje warning
                messages.error(request, '¡Usuario desconocido o password incorrecta!')
                return HttpResponseRedirect('/login/')
        else:
            # Mensaje de error
            messages.error(request, '¡Usuario desconocido o password incorrecta!')
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')

@login_required(login_url = login_var)
def applogout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url = login_var)
def resumen(request):
    return render(request, 'ibsadmin/resumen.html')
