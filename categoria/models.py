from django.db import models
from empresa.models import Empresa

# Create your models here.
class Categoria(models.Model):
	categoria = models.CharField(max_length=100)
	id_empresa = models.ForeignKey(Empresa, blank=True, null=True)

	def __str__(self):
		return self.categoria

	class Meta:
		ordering = ('categoria',)
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'
