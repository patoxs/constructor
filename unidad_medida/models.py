from django.db import models
from empresa.models import Empresa

# Create your models here.
class UnidadMedida(models.Model):
	nombre = models.CharField(max_length=100)
	unidad_medida = models.CharField(max_length=20)
	id_empresa = models.ForeignKey(Empresa, blank=True, null=True)

	def __str__(self):
		return self.unidad_medida

	class Meta:
		ordering = ('unidad_medida',)
		verbose_name = 'Unidad de medida'
		verbose_name_plural = 'Unidades de medida'