from django.db import models
from empresa.models import Empresa

# Create your models here.
class Impuesto(models.Model):
	nombre = models.CharField(max_length=200)
	valor = models.IntegerField()
	id_empresa = models.ForeignKey(Empresa, blank=True, null=True)


	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Impuesto'
		verbose_name_plural = 'Impuestos'