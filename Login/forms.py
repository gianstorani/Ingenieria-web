from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models
from .models import *


class RegisterForm(forms.Form):
    usuario = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'validate form-control','placeholder': ' Usuario'}))
    nombre = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class' : 'validate form-control','placeholder': ' Nombre'}))
    apellido = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'validate form-control','placeholder': ' Apellido'}))
    email = forms.EmailField(max_length=50 , widget=forms.TextInput(attrs={'class' : 'validate form-control','placeholder': ' Correo'}))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'validate form-control','placeholder ': ' Contraseña'}))
    confirmarcontraseña =forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'validate form-control','placeholder': ' Confirme contraseña'}))
    

