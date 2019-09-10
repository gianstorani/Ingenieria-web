from django.shortcuts import render
from .forms import PublicacionForm
from django.contrib.auth.decorators import login_required	
from .models import Publicacion
from Login.models import Perfil
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

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
        		tipoPublicacion = tipoPublicacion,
        		tituloPublicacion = tituloPublicacion,
        		precio = precio,
        		Contenido = Contenido,
        		idUsuarioPublicacion = idUsuarioPublicacion
        		)
		publicacion.save()
	else:
		form = PublicacionForm(request.POST)

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
	_usuario = request.user.id
	perfilesUsuario = Perfil.objects.all().filter(usuario = _usuario)
	for _perfil in perfilesUsuario:
		usuario.append(Perfil.objects.all().last())
	return render(request, 'verpublicacion.html', {'publicacion': publicacion,'form': form,'usuario': usuario })