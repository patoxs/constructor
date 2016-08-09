from django.db import models
from mandante.models import mandante
from empresa.models import Empresa

# Create your models here.
class Obra(models.Model):
	nombre = models.CharField(max_length=200)
	fecha_contrato = models.DateField()
	fecha_inicio = models.DateField()
	fecha_final = models.DateField()
	direccion = models.CharField(max_length=200)
	comuna = models.CharField(max_length=100)
	correo = models.EmailField()
	telefono = models.IntegerField()
	archivo = models.ImageField(blank=True)
	id_empresa = models.ForeignKey(Empresa, blank=True, null=True)
	id_mandante = models.ForeignKey(mandante, blank=True, null=True)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ('nombre',)
		verbose_name = 'Obra'
		verbose_name_plural = 'Obras'