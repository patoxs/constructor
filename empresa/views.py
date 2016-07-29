from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Empresa
# Create your views here.

def index(request):
	empresa = Empresa.objects.order_by('id')
	template = loader.get_template('index.html')
	contexto = {
		'empresa': empresa
	}
	return HttpResponse(template.render(contexto,request))
	