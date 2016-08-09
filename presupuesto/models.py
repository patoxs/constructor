from django.db import models
from obra.models import Obra
from empresa.models import Empresa
from tipo_presupuesto.models import TipoPresupuesto

# Create your models here.
class Presupuesto(models.Model):
	nombre = models.CharField(max_length=200)
	fecha_confeccion = models.DateField()
	fecha_ultima_modificacion = models.DateField()
	divisa = models.CharField(max_length=100)
	gasto_general = models.IntegerField()
	utilidad = models.IntegerField()
	redondeo = models.IntegerField()
	decimal = models.IntegerField()
	valor_total = models.IntegerField()
	id_empresa = models.ForeignKey(Empresa, blank=True, null=True)
	id_obra = models.ForeignKey(Obra, blank=True, null=True)
	id_tipo_presupuesto = models.ForeignKey(TipoPresupuesto, blank=True, null=True)


	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ('nombre','fecha_confeccion','valor_total',)
		verbose_name = 'Presupuesto'
		verbose_name_plural = 'Presupuestos'