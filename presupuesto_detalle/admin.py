from django.contrib import admin
from .models import PresupuestoDetalle

# Register your models here.
@admin.register(PresupuestoDetalle)
class AdminPresupuestoDetalle(admin.ModelAdmin):
	list_display = ('partida_interno','partida_externo','cantidad','precio_unitario','precio_total',)
	list_filter = ('id_presupuesto','id_partida',)
