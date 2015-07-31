# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import *
from .forms import *

# Variable por defecto para login requerido
login_var = '/login/'

# Vista inicial de la aplicacion
def index(request):
    return render_to_response('ibsadmin/index.html', {'messages': messages}, context_instance = RequestContext(request))  

# Vista de contacto
def contact(request):
    con_form = contact_form()
    if request.method == 'POST':
        messages.success(request, 'Gracias por contactarnos, lo contactaremos a la brevedad')
        return HttpResponseRedirect('/contacto/')
    return render_to_response('ibsadmin/contact.html', {'contact_form': con_form}, context_instance = RequestContext(request))    

# Vistas encargadas de manejar el login y logout
def applogin(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/resumen/')
    loginForm = login_form()
    return render_to_response('ibsadmin/login.html',{'login_form': loginForm, 'user': request.user}, context_instance = RequestContext(request))

def login_process(request):
    if not request.user.is_anonymous():
        messages.success(request, '¡Bienvenido!')
        return HttpResponseRedirect('/resumen/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redireccionar a vista de Resumen
                messages.success(request, '¡Bienvenido!')
                return HttpResponseRedirect('/resumen/')
            else:
                # Mensaje Warning
                messages.error(request, '¡Usuario desconocido o password incorrecta!')
                return HttpResponseRedirect('/login/')
        else:
            # Mensaje de Error
            messages.error(request, '¡Usuario desconocido o password incorrecta!')
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')

@login_required(login_url = login_var)
def applogout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Opciones de modificacion de usuario una vez logeado
@login_required(login_url = login_var)
def perfil(request):
    active_user = request.user
    if request.method == 'POST':
        user_form = user_mod_form(request.POST, request.FILES, instance = request.user)
        if user_form.is_valid() and request.POST['first_name'] != '' and request.POST['last_name'] != '':
            messages.success(request, '¡Perfil editado exitosamente!')
            user_form.save()
            return HttpResponseRedirect('/perfil/')
        else:
            messages.error(request, '¡Error en los parámetros ingresados!')
            return HttpResponseRedirect('/perfil/')
    else:
        user_form = user_mod_form(instance = request.user)    
    return render_to_response('ibsadmin/perfil.html',{'user_form': user_form,'user': request.user}, context_instance = RequestContext(request))

@login_required(login_url = login_var)
def password_change(request):
    password_form = password_change_form()
    if request.method == 'POST':
        user_password = request.user.password
        old_password = request.POST['old_password']
        if check_password(old_password, request.user.password):
            new_password = request.POST['new_password']
            new_password_two = request.POST['new_password_two']
            if new_password == new_password_two:
                active_user = User.objects.get(username = request.user)
                active_user.set_password(new_password)
                active_user.save()
                messages.success(request, '¡Clave modificada exitosamente!')
            else:
                messages.error(request, '¡La nueva clave no coincide!')
        else:
            # Mensaje de Error
            messages.error(request, '¡La clave ingresada no corresponde a la clave actual!')
    return render_to_response('ibsadmin/password_change.html',{'password_form': password_form,'user': request.user}, context_instance = RequestContext(request))

# Opciones de usuario logeado
@login_required(login_url = login_var)
def resumen(request):
    return render(request, 'ibsadmin/resumen.html')
