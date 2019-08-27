from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User


class EstadoUsuario(models.Model):
	descripcion	= models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.descripcion


class TipoUsuario(models.Model):
	descripcion	=  models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.descripcion


class Perfil(models.Model):
	direccion = models.CharField(max_length=50, null=True, blank=True)
	direccionNumero = models.IntegerField(default=0)
	ciudad	= models.CharField(max_length=50, null=True, blank=True)
	provincia = models.CharField(max_length=50, null=True, blank=True)
	pais = models.CharField(max_length=50, null=True, blank=True)
	fechaNacimiento = models.DateField(null=True, blank=True)
	usuario = models.OneToOneField(User,on_delete = models.CASCADE, null=True, blank=True)
	idEstadoUsuario	= models.ForeignKey(EstadoUsuario,on_delete = models.CASCADE, null=True, blank=True)
	idTipoUsuario	= models.ForeignKey(TipoUsuario,on_delete = models.CASCADE, null=True, blank=True)
	activacion_token = models.CharField(max_length = 40, blank = True, null = True)
	olvido_token = models.CharField(max_length = 40, blank = True, null = True)
	fechaBaja = models.DateTimeField(null=True,blank=True)


	def __str__(self):
		return self.usuario.username