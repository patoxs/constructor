from django.conf.urls import url
from empresa.views import *

empresa = EmpresaList.as_view()

urlpatterns = [
	url(r'^empresa/$',empresa,name='empresa'),
	url(r'^empresa/(?P<id>\d+)/$',empresa,name='empresa')
]