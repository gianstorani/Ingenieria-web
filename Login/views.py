from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth import login as auth_login
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import FormView
from django.template import RequestContext
from django.contrib.auth.decorators import login_required	
import hashlib, datetime, random
import os, string
from .models import Perfil
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm



def logout(request):
    try:
        print("ok")
        auth_logout(request)
    except Exception as e:
        print(e)
    return HttpResponseRedirect("/portada/")


def registrar(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if not User.objects.filter(username=request.POST['usuario']).exists():
			if not User.objects.filter(email=request.POST['email']).exists():
				if request.POST['contraseña'] == request.POST['confirmarcontraseña']:
					usuario = request.POST['usuario']
					nombre = request.POST['nombre']
					apellido = request.POST['apellido']
					email  = request.POST['email']
					contraseña = request.POST['contraseña']
					user = User.objects.create_user(username=usuario,first_name = nombre, last_name = apellido, email=email, password=contraseña)
					user.save()
					user.is_active  = False

					N = 25
					token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
					perfil = Perfil(usuario = user, activacion_token = token)

					email_subject   = 'Confirmación de cuenta AlquileresYA!'
					email_body      = "Hola %s, Gracias por registrarte. Para activar tu cuenta haga clíck en este link: http://127.0.0.1:8000/bienvenido/%s" % (nombre, token) 	

					send_mail(email_subject,email_body, 'proyecto.alquileres19@gmail.com',[email] )

					user.save()
					perfil.save()


					return HttpResponseRedirect("validacionmail/")
				else:
					messages.error(request, "Las contraseñas ingresadas no son iguales")
			else:
				messages.error(request, "El correo ingresado ya se encuentra registrado")
		else:
			messages.error(request, "El nombre de usuario ya se encuentra registrado")
	else:
		form = RegisterForm()
	return render(request,'registrar.html', { 'form': form })


        
def portada(request):
    return render(request, 'portada.html')


def bienvenido(request):
    return render(request, 'bienvenido.html')

def validacionmail(request):
    return render(request, 'validacionmail.html')

def confirmar(request, activacion_token):
	#tratar de no arrojar 404 y tirar un mensaje de token invalido
	try:
	    perfil_usuario = get_object_or_404(Perfil, activacion_token = activacion_token )    
	    user  = perfil_usuario.usuario
	    user.is_active  = True
	    user.save()
	    auth_login(request,user)
	    
	except:
		messages.error(request, "Token invalido o el mismo ya expiró")
	return render(request, 'bienvenido.html')


@login_required
def nosotros(request):
    return render(request, 'nosotros.html')



def editarusuario(request):
	return render(request, "editarusuario.html")








