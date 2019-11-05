from django import forms
from django.contrib.auth.models import User
from . models import *
from django.db import models
from django.forms import ModelForm, Textarea

tipoPubli = (
    ('Electronica', 'Electronica'),
    ('Equipamiento','Equipamiento'),
    ('Maquinarias','Maquinarias'),
    ('Telefonia','Telefonia'),
    ('Electronica','Electronica'),
    ('Informatica','Informatica'),
    ('AudioVideo','Audio y video'),
    ('Juegos','Juegos'),
    ('Electrodomesticos','Electrodomesticos'),
    ('Amoblamientos','Amoblamientos'),
    ('Herramientas','Herramientas'),
    ('Bazar','Bazar'),
)

class PublicacionForm(forms.Form):
	tipoPublicacion = forms.CharField(max_length=50, widget=forms.Select(choices=tipoPubli, attrs={'class' : 'validate form-control '}))
	tituloPublicacion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'validate form-control'}))
	precio = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class' : 'validate form-control'}))
	Contenido = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={"rows":10, "cols":20,'class' : 'validate form-control'}))
	localidad = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'validate form-control'}))
	provincia = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'validate form-control'}))
	imagen = forms.ImageField()

class ComentarioForm(forms.Form):
    ContenidoComentario = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={"rows":10, "cols":20,'class' : 'validate form-control'}))

class RespuestaForm(forms.Form):
    ContenidoRespuesta = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={"rows":10, "cols":20,'class' : 'validate form-control'}))
