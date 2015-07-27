# -*- encoding: utf-8 -*-
from django import forms
from django.forms.widgets import Input
from ibsadmin.models import *

class login_form(forms.Form):
    username = forms.CharField(
    	widget=forms.TextInput(attrs={'placeholder': '12345678-9'})
    	)
    password = forms.CharField(
    	widget=forms.PasswordInput(attrs={'placeholder': '*****'})
    	)