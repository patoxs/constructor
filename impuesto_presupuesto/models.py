from django.db import models
from impuesto.models import Impuesto
from presupuesto.models import Presupuesto

# Create your models here.
class ImpuestoPresupuesto(models.Model):
	id_presupuesto = models.ForeignKey(Presupuesto, blank=True, null=True)
	id_impuesto = models.ForeignKey(Impuesto, blank=True, null=True)

