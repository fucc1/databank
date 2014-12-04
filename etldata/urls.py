from django.conf.urls import patterns, url

from etldata import views

urlpatterns = patterns('',
	url(r'^download/', views.download), 
	url(r'^full_export/', views.full_export), 
	url(r'^export/', views.export), 
)