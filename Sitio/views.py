from django.shortcuts import render
from .forms import PublicacionForm, ComentarioForm
from django.contrib.auth.decorators import login_required
from .models import Publicacion, Comentario
from Login.models import Perfil
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

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
		imagen = request.FILES['imagen']
		publicacion = Publicacion(
			imagen=imagen,
			tipoPublicacion = tipoPublicacion,
			tituloPublicacion = tituloPublicacion,
			precio = precio,
			Contenido = Contenido,
			idUsuarioPublicacion = idUsuarioPublicacion
        )
		publicacion.save()

		# return HttpResponseRedirect("/mispublicaciones")

		_usuario = request.user.id
		mispublicaciones = Publicacion.objects.all().filter(idUsuarioPublicacion = _usuario)
		return render(request, 'mispublicaciones.html', {'mispublicaciones': mispublicaciones})
	else:
		form = PublicacionForm(request.POST)

	usuario  = []
	_usuario = request.user.id
	perfilesUsuario = Perfil.objects.all().filter(usuario = _usuario)
	for _perfil in perfilesUsuario:
		usuario.append(Perfil.objects.all().last())

	return render(request, 'nuevapublicacion.html',{ 'form': form ,'usuario': usuario})

def portada(request):
	lista_publicacion = Publicacion.objects.all()
	return render(request, 'portada.html', {'lista_publicacion' : lista_publicacion})


def mispublicaciones(request):
	_usuario = request.user.id
	mispublicaciones = Publicacion.objects.all().filter(idUsuarioPublicacion = _usuario)
	return render(request, 'mispublicaciones.html', {'mispublicaciones': mispublicaciones})


def verpublicacion(request,pk):
	form = PublicacionForm(request.POST)
	_idPublicacion = pk
	publicacion = Publicacion.objects.all().filter(idPublicacion = _idPublicacion).first()

	if request.method == 'POST':
		model = Comentario
		contenidoComentario = request.POST.get('ContenidoComentario')
		idUsuarioComentario = request.user
		comentario = Comentario(
			    idUsuarioComentario = idUsuarioComentario,
			    idPublicacion = publicacion,
			    contenidoComentario = contenidoComentario
        		)
		comentario.save()

		return HttpResponseRedirect('/verpublicacion/%s' %pk )

	else:

		form = ComentarioForm()

		usuario = publicacion.idUsuarioPublicacion
		perfilUsuario = Perfil.objects.all().filter(usuario = usuario).first()

		return render(request, 'verpublicacion.html',
		{'publicacion': publicacion,'form': form,'user': usuario, 'perfil': perfilUsuario})
