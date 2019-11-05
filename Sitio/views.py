from django.shortcuts import render
from .forms import PublicacionForm, ComentarioForm, RespuestaForm
from django.contrib.auth.decorators import login_required
from .models import Publicacion, Comentario, Respuesta, PuntajeNegativo, PuntajePositivo
from Login.models import Perfil
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from ProyectoAlquileres.serializers import PublicacionSerializer

# Create your views here.
class PublicacionesSet(viewsets.ModelViewSet):
	queryset = Publicacion.objects.all()#.order_by('FechaPublicacion')
	serializer_class = PublicacionSerializer

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

		puntajepositivo = PuntajePositivo.objects.all().filter(idPublicacion = publicacion).count()
		puntajenegativo = PuntajeNegativo.objects.all().filter(idPublicacion = publicacion).count()
		usuario = publicacion.idUsuarioPublicacion
		perfilUsuario = Perfil.objects.all().filter(usuario = usuario).first()

		return render(request, 'verpublicacion.html',
		{'publicacion': publicacion,'form': form,'user': usuario, 'perfil': perfilUsuario,
		'puntajepositivo': puntajepositivo, 'puntajenegativo' : puntajenegativo})

def editarpublicacion(request,pk):
	model = Publicacion
	form = PublicacionForm(request.POST)
	_idPublicacion = pk
	publicacion = Publicacion.objects.all().filter(idPublicacion = _idPublicacion).first()

	if request.user == publicacion.idUsuarioPublicacion:
		if request.method == 'POST':
			form = PublicacionForm(request.POST)
			tipoPublicacion = request.POST['tipoPublicacion']
			tituloPublicacion = request.POST['tituloPublicacion']
			precio = request.POST['precio']
			contenido = request.POST['contenido']
			publicacion.tipoPublicacion = tipoPublicacion
			publicacion.tituloPublicacion = tituloPublicacion
			publicacion.precio = precio
			publicacion.Contenido = contenido
			publicacion.save()
			return HttpResponseRedirect('/verpublicacion/%s' %pk  )
		else:
			usuario = publicacion.idUsuarioPublicacion
			perfilUsuario = Perfil.objects.all().filter(usuario = usuario).first()

			return render(request, 'editarpublicacion.html',
			{'publicacion': publicacion,'form': form,'user': usuario, 'perfil': perfilUsuario})
	else:
		return HttpResponseRedirect("/errorpage")

def respondercomentario(request,pk):
	model = Respuesta
	_idComentario = pk
	comentario = Comentario.objects.all().filter(idComentario = _idComentario).first()

	if request.user == comentario.idPublicacion.idUsuarioPublicacion:
		if request.method == 'POST':
			model = Respuesta
			idUsuario = request.user
			contenidoRespuesta = request.POST.get('ContenidoRespuesta')
			respuesta = Respuesta(
	            idComentario = comentario,
	            idUsuario = idUsuario,
	            contenidoRespuesta = contenidoRespuesta
	        )
			respuesta.save()

			pk = comentario.idPublicacion.idPublicacion
			return HttpResponseRedirect('/verpublicacion/%s' %pk )

		else:
			form = RespuestaForm()

			comentario = Comentario.objects.all().filter(idComentario = pk).first()
			usuario = comentario.idUsuarioComentario
			publicacion = comentario.idPublicacion

			return render(request, 'respondercomentario.html',
	        { 'form': form ,'usuario': usuario, 'comentario': comentario, 'publicacion': publicacion})
	else:
		return HttpResponseRedirect("/errorpage")

def errorpage(request):
	return render(request, 'errorpage.html')
