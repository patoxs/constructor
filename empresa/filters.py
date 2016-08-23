import django_filters
from rest_framework import filters
from .models import Empresa


class EmpresaFilter(filters.FilterSet):
    class Meta:
        model = Empresa
        fields = ['empresa', 'representate']
