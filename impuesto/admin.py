from django.contrib import admin
from .models import Impuesto
# Register your models here.

@admin.register(Impuesto)
class AdminImpuesto(admin.ModelAdmin):
	list_display = ('nombre','valor',)
	list_filter = ('id_empresa',)
