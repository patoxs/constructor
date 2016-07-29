from django.contrib import admin
from .models import Empresa

# Register your models here.
# admin.site.register(Empresa)
@admin.register(Empresa)
class AdminEmpresa(admin.ModelAdmin):
	list_display = ('empresa','email','telefono',)
	list_filter = ('empresa',)