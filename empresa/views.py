from .models import Empresa
from django.shortcuts import get_object_or_404
from .serializers import EmpresaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


class EmpresaList(APIView):
    serializer_class = EmpresaSerializer

    def get(self, request, id=None, format=None):
        if id is not None:
            empresa = get_object_or_404(Empresa, pk=id)
            todos = False
        else:
            empresa = Empresa.objects.all()
            todos = True
        respuesta = EmpresaSerializer(empresa, many=todos)
        return Response(respuesta.data)

    def post(self, request, id=None, format=None):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class EmpresaViewset(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()

# lookup_field = 'id'

# empresa_list = EmpresaViewset.as_view({'get':'list'})
# empresa_detail = EmpresaViewset.as_view({'get':'retrieve'})
