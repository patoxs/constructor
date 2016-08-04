from django.db import models
from tipo_usuario.models import tipo_usuario
from empresa.models import Empresa

# Create your models here.
class Usuario(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	login = models.CharField(max_length=100)
	clave = models.CharField(max_length=100)
	activo = models.IntegerField()
	id_tipo_usuario = models.ForeignKey(tipo_usuario, blank=True, null=True)
	id_empresa = models.ForeignKey(Empresa, blank=True, null=True)

	def __str__(self):
		return self.login

	class Meta:
		ordering = ('login',)
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'