from urlparse import urlparse
from etldata.models import DataConnection
from django.views import generic
from django.http import HttpResponse
from StringIO import StringIO
import csv

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
	apis = DataConnection.objects.values('webservice')
	
	fileHandle = StringIO()
	a = csv.writer(fileHandle)
	data = [['Databank Report',''],['',''],['Number of Indicators',length],['Not Checked',lengthNotChecked],['Viewed',lengthViewed],['Data Begin Date',oldest],['Data End Date',newest],['',''],['Sectors','']]
	
	for sectorName in sectors:
		strSector = sectorName.get('sector')
		filtered = dataConnections.filter(sector=strSector)
		lenFiltered = len(filtered)
		sectorArray = [strSector , lenFiltered]
		data.append(sectorArray)
	
	apiHeader=['','']
	data.append(apiHeader)
	apiHeader=['APIs','']
	data.append(apiHeader)
	
	for api in apis:
		strApi = api.get('webservice')
		if(len(strApi)>0):
			urlObj = urlparse(strApi)
			netLoc=urlObj.netloc
			filtered = dataConnections.filter(webservice__icontains=netLoc)
			lenFiltered=len(filtered)
			apiArray = [netLoc, lenFiltered]
			data.append(apiArray)
			
	a.writerows(data)
		
	filestring = fileHandle.getvalue()
	fileHandle.close()
	
	resp = HttpResponse(filestring, mimetype='application/x-download')
	resp['Content-Disposition'] = 'attachment;filename=databank_report.csv'
	return resp
	
