from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
#from empresa.views import EmpresaViewset
from empresa import views

router = DefaultRouter()
router.register(r'empresa', views.EmpresaViewset)

urlpatterns = [
	url(r'^', include(router.urls)),
]
