from django.contrib import admin
from .models import UnidadMedida

# Register your models here.
@admin.register(UnidadMedida)
class AdminUnidadMedida(admin.ModelAdmin):
	list_display = ('nombre','unidad_medida',)
