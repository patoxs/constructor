from django.contrib import admin
from .models import Presupuesto
# Register your models here.

@admin.register(Presupuesto)
class AdminPresupuesto(admin.ModelAdmin):
	list_display = ('nombre','fecha_confeccion','valor_total',)
	list_filter = ('fecha_confeccion',)