from django.shortcuts import render
from .forms import PublicacionForm
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required	
=======
from django.contrib.auth.decorators import login_required
>>>>>>> nicolas
from .models import Publicacion
from Login.models import Perfil
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
<<<<<<< HEAD
=======
from django.http import HttpResponseRedirect
>>>>>>> nicolas

# Create your views here.

@login_required
def nuevapublicacion(request):
	model = Publicacion
	if request.method == 'POST':
		form = PublicacionForm(request.POST)
		tipoPublicacion = request.POST['tipoPublicacion']
		tituloPublicacion = request.POST['tituloPublicacion']
		precio = request.POST['precio']
		Contenido = request.POST['Contenido']
		idUsuarioPublicacion = request.user
<<<<<<< HEAD
		try:
			publicacion = Publicacion(
        		tipoPublicacion = tipoPublicacion,
        		tituloPublicacion = tituloPublicacion,
        		precio = precio,
        		Contenido = Contenido,
        		idUsuarioPublicacion = idUsuarioPublicacion
        		)
		except Exception as e:
			publicacion = Publicacion(
=======
		publicacion = Publicacion(
>>>>>>> nicolas
        		tipoPublicacion = tipoPublicacion,
        		tituloPublicacion = tituloPublicacion,
        		precio = precio,
        		Contenido = Contenido,
        		idUsuarioPublicacion = idUsuarioPublicacion
        		)
		publicacion.save()
<<<<<<< HEAD
	else:
		form = PublicacionForm(request.POST)
=======
		return HttpResponseRedirect("/nuevapublicacion")

	else:
		form = PublicacionForm()
>>>>>>> nicolas

	usuario  = []
	_usuario = request.user.id
	perfilesUsuario = Perfil.objects.all().filter(usuario = _usuario)
	for _perfil in perfilesUsuario:
		usuario.append(Perfil.objects.all().last())

	return render(request, 'nuevapublicacion.html',{ 'form': form ,'usuario': usuario})


def mispublicaciones(request):
	_usuario = request.user.id
	mispublicaciones = Publicacion.objects.all().filter(idUsuarioPublicacion = _usuario)
	return render(request, 'mispublicaciones.html', {'mispublicaciones': mispublicaciones})


def verpublicacion(request,pk):
	form = PublicacionForm(request.POST)
	_idPublicacion = pk
	publicacion = Publicacion.objects.all().filter(idPublicacion = _idPublicacion)

	usuario  = []
<<<<<<< HEAD
	_usuario = request.user.id
	perfilesUsuario = Perfil.objects.all().filter(usuario = _usuario)
	for _perfil in perfilesUsuario:
		usuario.append(Perfil.objects.all().last())
	return render(request, 'verpublicacion.html', {'publicacion': publicacion,'form': form,'usuario': usuario })
=======
	for public in publicacion:
		_usuario = public.idUsuarioPublicacion
	perfilesUsuario = Perfil.objects.filter(usuario = _usuario).last()
	return render(request, 'verpublicacion.html', {'publicacion': publicacion,'form': form,'perfilesUsuario': perfilesUsuario })
>>>>>>> nicolas
