from django.contrib import admin
from .models import Partida
# Register your models here.

@admin.register(Partida)
class AdminPartida(admin.ModelAdmin):
	list_display = ('partida','unidad',)