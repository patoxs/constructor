from django.conf.urls import url
from rest_framework import routers
from empresa.views import EmpresaViewSet

from empresa import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.empresa_detalle),
	url(r'^nuevo', views.nueva_empresa, name="empresa_nueva"),
]

router = routers.DefaultRouter()
router.register(r'empresa', EmpresaViewSet)

urlpatterns = router.urls