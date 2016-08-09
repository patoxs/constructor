from django.db import models
from empresa.models import Empresa

# Create your models here.
class TipoPresupuesto(models.Model):
	tipo_presupuesto = models.CharField(max_length=200)
	id_empresa = models.ForeignKey(Empresa, blank=True, null=True)

	def __str__(self):
		return self.tipo_presupuesto

	class Meta:
		ordering = ('tipo_presupuesto',)
		verbose_name = 'Tipo de presupuesto'
		verbose_name_plural = 'Tipos de presupuesto'