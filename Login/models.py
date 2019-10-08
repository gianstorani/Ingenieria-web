from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User

class Perfil(models.Model):
	estadoUsuario = (
		('Pendiente','Pendiente de activación'),
		('Activo','Activo'),
		('Suspendido','Suspendido'),
		('Eliminado','Eliminado'),
		)
	tipoUsuario = (
        ('Administrador','Administrador'),
        ('Visitante','Visitante'),
    	)
	direccion = models.CharField(max_length=50, null=True, blank=True)
	telefonoNumero = models.CharField(max_length=50, null=True, blank=True)
	ciudad	= models.CharField(max_length=50, null=True, blank=True)
	provincia = models.CharField(max_length=50, null=True, blank=True)
	pais = models.CharField(max_length=50, null=True, blank=True)
	fechaNacimiento = models.DateField(null=True, blank=True)
	usuario = models.ForeignKey(User,on_delete = models.CASCADE, null=True, blank=True)
	idEstadoUsuario	= models.CharField(choices=estadoUsuario, null=True, blank=True, default='Pendiente',max_length=60)
	idTipoUsuario = models.CharField(choices=tipoUsuario, null=True, blank=True, default='Visitante',max_length=60)
	activacion_token = models.CharField(max_length = 40, blank = True, null = True)
	olvido_token = models.CharField(max_length = 40, blank = True, null = True)
	fechaBaja = models.DateTimeField(null=True,blank=True)


	def __str__(self):
		return self.usuario.username