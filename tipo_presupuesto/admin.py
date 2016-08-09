from django.contrib import admin
from .models import TipoPresupuesto

# Register your models here.
@admin.register(TipoPresupuesto)
class AdminTipoPrespuesto(admin.ModelAdmin):
	list_display = ('tipo_presupuesto',)