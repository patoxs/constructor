from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Empresa
from .serializers import EmpresaSerializer



# from .forms import EmpresaNueva

# from .models import Empresa
# # Create your views here.

# def index(request):
# 	empresa = Empresa.objects.order_by('id')
# 	template = loader.get_template('index.html')
# 	contexto = {
# 		'empresa': empresa
# 	}
# 	return HttpResponse(template.render(contexto,request))
	
# def empresa_detalle(request, pk):
# 	empresa = get_object_or_404(Empresa, pk=pk)
# 	template = loader.get_template('empresa_detalle.html')
# 	contexto = {
# 		'empresa': empresa
# 	}
# 	return HttpResponse(template.render(contexto, request))

# def nueva_empresa(request):
# 	if request.method == 'POST':
# 		form = EmpresaNueva(request.POST, request.FILES)
# 		if form.is_valid():
# 			product = form.save()
# 			product.save()
# 			return HttpResponseRedirect('/')
# 	else:
# 		form = EmpresaNueva()

# 	template = loader.get_template('empresa_nueva.html')
# 	contexto = {
# 		'form': form
# 	}
# 	return HttpResponse(template.render(contexto, request))


#empresa/
class EmpresaList(APIView):

	serializer_class = EmpresaSerializer

	def get(self, request, id=None, format=None):
		if id != None:
			empresa = get_object_or_404(Empresa,pk=id)
			todos = False
		else:
			empresa = Empresa.objects.all()
			todos = True
		
		respuesta = EmpresaSerializer(empresa, many=todos)
		return Response(respuesta.data)

	def post(self):
		pass