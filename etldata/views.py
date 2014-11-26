from django.shortcuts import render

from django.shortcuts import render
from etldata.models import DataConnection
from django.views import generic
from django.http import HttpResponse
from StringIO import StringIO
import urllib2, json, csv
import codecs

def export(request):
	
	dataConnections = DataConnection.objects.all()
	length = len(dataConnections)
	
	notChecked = dataConnections.filter(status='Not Checked')
	lengthNotChecked = len(notChecked)
	
	viewed = dataConnections.filter(status='Viewed')
	lengthViewed = len(viewed)
	
	completed = dataConnections.filter(status='Completed')
	lengthCompleted = len(completed)
	
	sortedStart = dataConnections.order_by('data_start')
	sortedEnd = dataConnections.order_by('-data_end')
	
	oldest = sortedStart[0].data_start
	newest = sortedEnd[0].data_end
	
	strSectors = []
	sectors = DataConnection.objects.values('sector')
	
	fileHandle = StringIO()
	a = csv.writer(fileHandle)
	data = [['Number of Indicators',length],['Not Checked',lengthNotChecked],['Viewed',lengthViewed],['Begin Date',oldest],['End Date',newest]]
	
	for sector in sectors:
		filtered = dataConnections.filter(status=sector)
		lenFiltered = len(filtered)
		strSector = sector.get('sector')
		strSectorDecoded=codecs.decode(strSector,'utf-8')
		strSectors = [strSectorDecoded , lenFiltered]
		data.append(strSectors)
	
	a.writerows(data)
	
	filestring = fileHandle.getvalue()
	fileHandle.close()
	
	resp = HttpResponse(filestring, mimetype='application/x-download')
	resp['Content-Disposition'] = 'attachment;filename=tableoutput.csv'
	return resp
	
