from django.conf.urls import url

from empresa import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]