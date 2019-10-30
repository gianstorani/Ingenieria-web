from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

# Create your models here.


class Publicacion(models.Model):
    tipoPublicacion = (
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
    estadoPublicacion = (
        ('Publicado','Publicado'),
        ('Borrador','Borrador'),
        ('Denunciado','Denunciado'),
        ('Eliminado','Eliminado'),
    )
    idPublicacion = models.AutoField(primary_key= True)
    idUsuarioPublicacion = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tituloPublicacion = models.CharField(blank=False, max_length = 50)
    tipoPublicacion = models.CharField(choices=tipoPublicacion, null=True, blank=True,max_length = 50)
    estadoPublicacion = models.CharField(choices=estadoPublicacion, null=True, blank=True,max_length = 50)
    Contenido = models.TextField(blank=False)
    precio = models.TextField(blank=False)
    FechaPublicacion = models.DateField(("Date"), auto_now=True, editable = False)
    FechaBajaPublicacion = models.DateField(default= None, editable = False,null = True)
    FechaModificacionPublicacion = models.DateField(default = None, editable = False, null = True)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True, default='#')

    def __str__(self):
        return (self.tituloPublicacion)


    def get_absolute_url(self):
        return reverse ('nuevapublicacion', args=[str(self.idPublicacion)])


class Comentario(models.Model):
    idComentario = models.AutoField(primary_key = True)
    idUsuarioComentario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    idPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    contenidoComentario = models.TextField(null = False)
    fechaComentario = models.DateField(("Date"), auto_now_add = True)
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

class Puntaje(models.Model):
    idPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    RATING_CHOICES = ((1, 'uno'), (2, 'dos'), (3, 'tres'), (4, 'cuatro'), (5, 'cinco'))
    #puntos = models.PositiveSmallIntegerField('Rating (stars)', null=True, blank=True, choices=RATING_CHOICES)

    def __str__(self):
        return self.contenidoPuntaje

class Denuncia(models.Model):
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    idComentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, null=True, blank=True)
    idPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, null=True, blank=True)
    fechaAltaDenuncia = models.DateTimeField(default=timezone.now, null=True)
    fechaBajaDenuncia = models.DateTimeField(null=True, blank=True)
    motivoBaja = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.contenidoComentario
