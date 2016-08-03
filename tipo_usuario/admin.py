from django.contrib import admin
from .models import tipo_usuario
# Register your models here.

@admin.register(tipo_usuario)
class AdminTipoUsuario(admin.ModelAdmin):
	list_display = ('tipo_usuario',)
	list_filter = ('tipo_usuario',)