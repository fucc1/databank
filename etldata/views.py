from urlparse import urlparse
from etldata.models import DataConnection
from django.views import generic
from django.http import HttpResponse
from django.template import loader, RequestContext
from StringIO import StringIO
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
import csv

@login_required
def download(request):
	dataConnections = DataConnection.objects.all()
	template = loader.get_template('download.html')
	context = RequestContext(request, {'dc': dataConnections,})
	return HttpResponse(template.render(context))

@login_required
def full_export(request):
	dataConnections = DataConnection.objects.all()
	first = dataConnections[0]
	data=[]
	row=[]

	headers = fields=model_to_dict(first)
	
	for field,val in fields.items():
		row.append(field)
	data.append(row)
	row=[]
	
	for dc in dataConnections:
		fields=model_to_dict(dc)
		for field,val in fields.items():
			row.append(val)
		data.append(row)
		row=[]
		
	fileHandle = StringIO()
	a = csv.writer(fileHandle)
	
	a.writerows(data)
		
	filestring = fileHandle.getvalue()
	fileHandle.close()
	
	resp = HttpResponse(filestring, mimetype='application/x-download')
	resp['Content-Disposition'] = 'attachment;filename=full_report.csv'
	
	return resp

@login_required
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
		if(sectorArray in data):
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
	
