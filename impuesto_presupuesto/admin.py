from django.contrib import admin
from .models import ImpuestoPresupuesto
# Register your models here.

@admin.register(ImpuestoPresupuesto)
class AdminImpuestoPresupuesto(admin.ModelAdmin):
	list_display = ('id_presupuesto','id_impuesto',)
	list_filter = ('id_presupuesto','id_impuesto',)
