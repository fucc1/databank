
from django.db import models

from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator




from processors.helpers import DATACONNECTION_TYPES
from etldata.enumerations import STATUS

from processors.models import Processor
#from openrefine.models import OpenRefine


from taggit.managers import TaggableManager





class MetaData(models.Model):

    title = models.CharField('Title', blank=True, max_length=255, help_text=_('Human-readable name of the asset. Should be in plain English and include sufficient detail to facilitate search and discovery.'))

    description = models.TextField(_('Description'), blank=True, help_text=_('Human-readable description (e.g., an abstract) with sufficient detail to enable a user to quickly understand whether the asset is of interest.'))

    keywords = TaggableManager(help_text=_('Tags (or keywords) help users discover your dataset; please include terms that would be used by technical and non-technical users.'), blank=True)

    modified = models.DateTimeField(_('Last Modified'), blank=True, auto_now=True, auto_now_add=False, help_text=_('Most recent date on which the dataset was changed, updated or modified.'))

    publisher = models.CharField('Publisher', blank=True, max_length=255, help_text=_('The publishing entity.'))

    contactpoint = models.CharField('Contact Point', blank=True, max_length=255, help_text=_('Contact person"s name for the asset.'))

    contactemail = models.EmailField('Publisher', blank=True, max_length=255, help_text=_('Contact persons email address.'))

    identifier = models.CharField('Identifier', blank=True, max_length=255, help_text=_('A unique identifier for the dataset or API as maintained within an Agency catalog or database.'))

    bureauCode = models.CharField('Bureau Code', blank=True, max_length=255, help_text=_('Federal agencies, combined agency and bureau code from OMB Circular A-11, Appendix C in the format of 015:11.'))

    programCode = models.CharField('Program Code', blank=True, max_length=255, help_text=_('Federal agencies, list the primary program related to this data asset, from the Federal Program Inventory. Use the format of 015:001'))

    accessLevelComment = models.TextField(_('Access Level Comment'), blank=True, help_text=_('An explanation for the selected "accessLevel" including instructions for how to access a restricted file, if applicable, or explanation for why a "non-public" or "restricted public" data asset is not "public," if applicable. Text, 255 characters.'))

    #also included in this accessURL and webService, but that can be gotten from the DataConnection model

    format = models.CharField('Format', blank=True, max_length=255, help_text=_('The file format or API type of the distribution.'))

    license = models.TextField(_('Access Level Comment'), blank=True, help_text=_('The license with which the dataset or API is published. See Open Licenses for more information.'))

    spatial = models.CharField('Spatial', blank=True, max_length=255, help_text=_('The range of spatial applicability of a dataset. Could include a spatial region like a bounding box or a named place.'))

    temporal = models.CharField('Temporal', blank=True, max_length=255, help_text=_('The range of temporal applicability of a dataset (i.e., a start and end date of applicability for the data).'))





class DataConnection(models.Model):

    #cases including
        #File upload
        #API end point without preprocessing
        #API end poitn with preprocessing
        #AQPI end point with preprocessing and OpenRefine

    alphanumeric = RegexValidator(r'^[\w\-\s]*$', 'Only alphanumeric characters are allowed.')

    indicator = models.CharField('Data Connection Name', max_length=300, help_text=_('Name of the indicator'), unique=True, validators=[alphanumeric])

    sectorid = models.CharField('Sector Indicator', blank=True, max_length=10, help_text=_('SectorID'))

    agency = models.CharField('Agency', blank=True, max_length=255, help_text=_('Agency'))

    organization = models.CharField('Organization', blank=True, max_length=255, help_text=_('organization'))


    metadataURL = models.URLField('Metadata URL', blank=True, help_text=_('The URl where the metadata is found'))

    update_freq = models.CharField(_('Update Frequency'), blank=True, max_length=255, help_text=_('Automatically pull in data from Formhub'))



    raw_response = models.TextField(_('Description'), blank=True, help_text='Raw response from data URL')

    orgURL = models.URLField('Information Page', blank=True, help_text=_('The URl where the data is found'))

    webservice = models.URLField('Web Service URL such as API', blank=True, help_text=_('The URL of the organization or information'))

    notes = models.TextField(_('Notes'), blank=True, help_text=_('Notes'))

    technicalnotes = models.TextField(_('Techincal Notes'), blank=True, help_text=_('Technical Notes'))

    units = models.CharField('Units', blank=True, max_length=255, help_text=_('Units'))

    metadata = models.ForeignKey(MetaData, blank=True, null=True)

    source = models.CharField('Source', blank=True, max_length=255, help_text=_('Units'))

    sector = models.CharField('Sector', blank=True, max_length=255, help_text=_('Sector'))

    downloadedFile = models.FileField(upload_to="rawdata", blank=True)

    preprocessors = models.ForeignKey(Processor, blank=True, null=True)

    status = models.CharField('Status', blank=False, max_length=255, help_text=_('Status'), choices=STATUS)

    #openrefine = models.ForeignKey(OpenRefine, blank=True, null=True)




