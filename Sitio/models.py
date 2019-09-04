from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Publicacion(models.Model):
    idPublicacion = models.AutoField(primary_key= True)
    idUsuarioPublicacion = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tituloPublicacion = models.CharField(blank=False, max_length = 50)
    Contenido = models.TextField(blank=False)
    FechaPublicacion = models.DateField(("Date"), auto_now=True, editable = False)
    FechaBajaPublicacion = models.DateField(default= None, editable = False,null = True)
    FechaModificacionPublicacion = models.DateField(default = None, editable = False, null = True)

    def __str__(self):
        return (self.Titulo)


class Comentario(models.Model):
    idComentario = models.AutoField(primary_key = True)
    idUsuarioComentario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    idPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    contenidoComentario = models.TextField(null = True)
    fechaComentario = models.DateField(("Date"), auto_now=True)
    fechaModiComentario = models.DateField(default = None, editable = False, null = True)
    fechaBajaComentario = models.DateField(default = None, editable = False, null = True)

    def __str__(self):
        return self.contenidoComentario

class Respuesta(models.Model):
	idComentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
	idUsuario = models.ForeignKey(User,on_delete=models.CASCADE)	
	contenidoRespuesta = models.TextField(null=True,blank=True)
	fechaBajaRespuesta = models.DateTimeField(auto_now=False, null=True, blank=True, default=None)
	fechaAltaRespuesta = models.DateTimeField(auto_now=False, null=True, blank=True, default=None)

	def __str__(self):
		return self.contenidoRespuesta



class Denuncia(models.Model):
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    idComentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, null=True, blank=True)
    idPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, null=True, blank=True)
    fechaAltaDenuncia = models.DateTimeField(default=timezone.now, null=True)
    fechaBajaDenuncia = models.DateTimeField(null=True, blank=True)
    motivoBaja = models.CharField(max_length=200, null=True, blank=True)

   
    def __str__(self):
        return self.contenidoComentario