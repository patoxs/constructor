from django.db import models

# Create your models here.
class mandante(models.Model):
	rut = models.IntegerField()
	digito_verificador = models.CharField(max_length=1)
	nombre = models.CharField(max_length=100)
	giro = models.CharField(max_length=255)
	comuna = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ('nombre',)
		verbose_name = 'Mandante'
		verbose_name_plural = 'Mandantes'