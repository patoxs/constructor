from django.contrib import admin
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class AdminUsuario(admin.ModelAdmin):
	list_display = ('apellido','nombre','login','activo',)
	list_filter = ('activo',)