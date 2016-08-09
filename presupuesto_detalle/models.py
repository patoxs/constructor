from django.db import models
from unidad_medida.models import UnidadMedida
from presupuesto.models import Presupuesto
from partida.models import Partida

# Create your models here.
class PresupuestoDetalle(models.Model):
	partida_interno = models.CharField(max_length=200)
	partida_externo = models.CharField(max_length=200)
	cantidad = models.IntegerField()
	precio_unitario = models.IntegerField()
	precio_total = models.IntegerField()
	id_unidad_medida = models.ForeignKey(UnidadMedida, blank=True, null=True)
	id_presupuesto = models.ForeignKey(Presupuesto, blank=True, null=True)
	id_partida = models.ForeignKey(Partida, blank=True, null=True, related_name='id_partida' )
	id_partida_padre = models.ForeignKey(Partida, blank=True, null=True, related_name='id_partida_padre')

	def __str__(self):
		return self.partida_interno

	class Meta:
		ordering = ('partida_interno','partida_externo',)
		verbose_name = 'Detalle presupuesto'
		verbose_name_plural = 'Detalle presupuesto'