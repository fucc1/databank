from django.contrib import admin
from django import forms
import reversion

# Register your models here.
from etldata.models import DataConnection, MetaData


class DataConnectionAdmin(admin.ModelAdmin):
    list_display = ('indicator','sectorid','organization','status',)
    #fieldsets =[(None,{'fields': ['categoryName']}),]

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude.append('preprocessors')
            self.exclude.append('raw_response')
        return super(DataConnectionAdmin, self).get_form(request, obj, **kwargs)



class MetaDataAdmin(reversion.VersionAdmin):
    list_display = ('title',)
    #fieldsets =[(None,{'fields': ['theme']}),]



admin.site.register(DataConnection, DataConnectionAdmin)
admin.site.register(MetaData, MetaDataAdmin)
