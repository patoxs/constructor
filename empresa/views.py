from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import EmpresaNueva

from .models import Empresa
# Create your views here.

def index(request):
	empresa = Empresa.objects.order_by('id')
	template = loader.get_template('index.html')
	contexto = {
		'empresa': empresa
	}
	return HttpResponse(template.render(contexto,request))
	
def empresa_detalle(request, pk):
	empresa = get_object_or_404(Empresa, pk=pk)
	template = loader.get_template('empresa_detalle.html')
	contexto = {
		'empresa': empresa
	}
	return HttpResponse(template.render(contexto, request))

def nueva_empresa(request):
	if request.method == 'POST':
		form = EmpresaNueva(request.POST, request.FILES)
		if form.is_valid():
			product = form.save()
			product.save()
			return HttpResponseRedirect('/')
	else:
		form = EmpresaNueva()

	template = loader.get_template('empresa_nueva.html')
	contexto = {
		'form': form
	}
	return HttpResponse(template.render(contexto, request))