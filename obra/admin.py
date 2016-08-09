from django.contrib import admin
from .models import Obra
# Register your models here.

@admin.register(Obra)
class AdminObra(admin.ModelAdmin):
	list_display = ('nombre','fecha_contrato','fecha_inicio','correo','telefono',)
	list_filter = ('fecha_inicio',)