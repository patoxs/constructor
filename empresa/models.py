from django.db import models

# Create your models here.

class Empresa(models.Model):
	empresa = models.CharField(max_length=100)
	rut = models.IntegerField()
	digito_verificador = models.CharField(max_length=1)
	email = models.EmailField(max_length=255)
	telefono = models.IntegerField()
	representate = models.CharField(max_length=255)
	logo = models.ImageField(blank=True)

	def __str__(self):
		return self.empresa

	class Meta:
		ordering = ('empresa',)
