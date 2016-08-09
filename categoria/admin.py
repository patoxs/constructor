from django.contrib import admin
from .models import Categoria
# Register your models here.

@admin.register(Categoria)
class AdminCategoria(admin.ModelAdmin):
	list_display = ('categoria',)
