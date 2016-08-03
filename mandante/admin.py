from django.contrib import admin
from .models import mandante
# Register your models here.

@admin.register(mandante)
class AdminMandante(admin.ModelAdmin):
	list_display = ('nombre','comuna',)
	list_filter = ('comuna',)