from django.db import models
from categoria.models import Categoria
from empresa.models import Empresa

# Create your models here.
class Partida(models.Model):
	partida = models.CharField(max_length=200)
	unidad = models.CharField(max_length=50)
	id_categoria = models.ForeignKey(Categoria, blank=True, null=True)
	id_empresa = models.ForeignKey(Empresa, blank=True, null=True)

	def __str__(self):
		return self.partida

	class Meta:
		ordering = ('partida',)
		verbose_name = 'Partida'
		verbose_name_plural = 'Partidas'