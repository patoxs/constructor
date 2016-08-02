from django import forms
from .models import Empresa


class EmpresaNueva(forms.ModelForm):
	class Meta:
		model = Empresa
		fields = '__all__'
