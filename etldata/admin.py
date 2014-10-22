from django.contrib import admin
from django import forms
import reversion

# Register your models here.
from etldata.models import DataConnection, MetaData


class DataConnectionAdmin(admin.ModelAdmin):
    list_display = ('indicator','sectorid','organization','status',)
    #fieldsets =[(None,{'fields': ['categoryName']}),]



class MetaDataAdmin(reversion.VersionAdmin):
    list_display = ('title',)
    #fieldsets =[(None,{'fields': ['theme']}),]



admin.site.register(DataConnection, DataConnectionAdmin)
admin.site.register(MetaData, MetaDataAdmin)
