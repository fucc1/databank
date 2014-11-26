from django.conf.urls import patterns, url

from etldata import views

urlpatterns = patterns('',
	url(r'^export/', views.export), 
)