from django.shortcuts import render
from .forms import PublicacionForm
from django.contrib.auth.decorators import login_required	
from .models import Publicacion
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
	return render(request, 'nuevapublicacion.html',{ 'form': form })


@login_required
def mispublicaciones(request):
	_usuario = request.user.id
	mispublicaciones = Publicacion.objects.all().filter(idUsuarioPublicacion = _usuario)
	return render(request, 'mispublicaciones.html', {'mispublicaciones': mispublicaciones})
