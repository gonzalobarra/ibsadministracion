# -*- encoding: utf-8 -*-
from django import forms
from django.forms.widgets import Input
from django.contrib.auth.models import User
from ibsadmin.models import *

# Form de login
class login_form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '12345678-9'})
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*****'})
        )

# Form de cambio de clave
class password_change_form(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*****'})
        )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*****'})
        )
    new_password_two = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*****'})
        )

# Form para modificar perfil
class user_mod_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email',)
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Juan'}),  
            'last_name': forms.TextInput(attrs={'placeholder': 'Perez'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ejemplo@ejemplo.com'}),        
        }

# Form para contacto
class contact_form(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Juan'})
        )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Perez'})
        )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'ejemplo@ejemplo.com'})
        )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows':'5'})
        )