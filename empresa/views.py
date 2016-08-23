from .filters import EmpresaFilter
from .models import Empresa
from django.shortcuts import get_object_or_404
from .serializers import EmpresaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters


# lookup_field = 'id'

# empresa_list = EmpresaViewset.as_view({'get':'list'})
# empresa_detail = EmpresaViewset.as_view({'get':'retrieve'})


class EmpresaViewset(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = EmpresaFilter




