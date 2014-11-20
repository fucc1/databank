from django.shortcuts import render
from etldata.models import DataConnection
from django.views import generic
from django.http import HttpResponse
import urllib2, json


def detail(request,id):
	
	poll = DataConnection.objects.get(pk=id)
	url = poll.webservice
	
	response = urllib2.urlopen(url);
	data = json.loads(response.read())
	s="<table border =\"1\">"
	s+="<tr><td>Indicator</td><td>Country</td><td>Value</td><td>Date</td></tr>"
	for r in data[1]:
		if(r['value']==None):
			r['value']="#"
			s+="<tr><td>" + r['indicator']['value'] + "</td><td>" + r['country']['value'] + "</td><td>" + r['value'] + "</td><td>" + r['date'] + "</td></tr>"
	s+="</table>"
	
	return HttpResponse(s)




