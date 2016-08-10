from django.contrib import admin
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class AdminUsuario(admin.ModelAdmin):
	list_display = ('nombre','apellido','login','activo',)
	list_filter = ('activo',)