from django.core.management.base import BaseCommand, CommandError
from etldata.models import DataConnection, MetaData

from optparse import make_option

import sys
import csv


class Command(BaseCommand):
    help = 'This will take whatever is available '
    option_list = BaseCommand.option_list + (make_option('--filepath',
                    action='store', dest='filepath',
                    help='This is the file that will be processed'),)


    def handle(self, *args, **options):

        filepath = options.get('filepath', None)

        if not filepath:
            print "you need a file path to load from the google drive"
            sys.exit(1)


        #iterate through the model and match things
        csvmapping = {
            "Sector": "sector",
            "Sector ID":"sectorid",
            "Agency":"agency",
            "Indicator":"indicator",
            "Units":"units",
            "Notes":"notes",
            "Web Site":"orgURL",
            "Organization":"organization",
            "File":"webservice",
            #"Downloaded":"",
            "edip-notes":"technicalnotes",
            #create new model for this
            "Unstructured Metadata":"",

        }

        with open(filepath, 'rb') as f:
            headers = []
            thereader = csv.reader(f)
            for row in thereader:
                if len(headers) == 0:
                    headers = row
                    continue

                tempobj = dict(zip(headers, row))

                try:
                    tempDataCon = DataConnection.objects.get(indicator=tempobj['Indicator'])
                except:
                    tempDataCon = None

                if tempDataCon:
                    print "skipping", tempobj['Indicator']
                    continue

                tempDataCon = DataConnection()



                for (csvhead,modelvar) in csvmapping.items():

                    if csvhead == "Unstructured Metadata":
                        if tempobj['Unstructured Metadata'] != "":
                            tempmeta = MetaData(title=tempobj['Unstructured Metadata'])
                            tempmeta.save()
                            setattr(tempDataCon, 'metadata', tempmeta)
                        #tempDataCon.metadata = tempmeta
                        continue
                    print modelvar, csvhead
                    setattr(tempDataCon, modelvar, tempobj[csvhead])



                tempDataCon.save()



