from django.db import models

# Create your models here.
class tipo_usuario(models.Model):
	tipo_usuario = models.CharField(max_length=100)

	def __str__(self):
		return self.tipo_usuario

	class Meta:
		ordering = ('tipo_usuario',)
		verbose_name = 'Tipo de Usuario'
		verbose_name_plural = 'Tipos de Usuario'