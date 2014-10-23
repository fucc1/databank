from django.contrib import admin
from django import forms
import reversion

# Register your models here.
from etldata.models import DataConnection, MetaData


class DataConnectionAdmin(reversion.VersionAdmin):
    list_display = ('indicator','sectorid','organization','status',)
    exclude = ('raw_response','preprocessors',)
    #fieldsets =[(None,{'fields': ['categoryName']}),]

    # def get_form(self, request, obj=None, **kwargs):
    #     if not request.user.is_superuser:
    #         self.exclude.append('preprocessors')
    #         self.exclude.append('raw_response')
    #     return super(DataConnectionAdmin, self).get_form(request, obj, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='superadmin').exists() or request.user.groups.filter(name='editor').exists():
            return self.readonly_fields

        if self.declared_fieldsets:
            return flatten_fieldsets(self.declared_fieldsets)
        else:
            return list(set(
                [field.name for field in self.opts.local_fields] +
                [field.name for field in self.opts.local_many_to_many]
            ))


    # def __init__(self, *args, **kwargs):
    #     super(DataConnectionAdmin, self).__init__(*args, **kwargs)
    #     self.list_display_links = (None,)


    # def has_add_permission(self, request, obj=None):
    #     if request.user.groups.filter(name='superadmin').exists() or request.user.groups.filter(name='editor').exists():
    #         return True
    #     else:
    #         return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     if request.user.groups.filter(name='superadmin').exists() or request.user.groups.filter(name='editor').exists():
    #         return True
    #     else:
    #         return False




class MetaDataAdmin(reversion.VersionAdmin):
    list_display = ('title',)
    #fieldsets =[(None,{'fields': ['theme']}),]


    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='superadmin').exists() or request.user.groups.filter(name='editor').exists():
            return self.readonly_fields

        if self.declared_fieldsets:
            return flatten_fieldsets(self.declared_fieldsets)
        else:
            return list(set(
                [field.name for field in self.opts.local_fields] +
                [field.name for field in self.opts.local_many_to_many]
            ))


    # def __init__(self, *args, **kwargs):
    #     super(MetaDataAdmin, self).__init__(*args, **kwargs)
    #     self.list_display_links = (None,)




admin.site.register(DataConnection, DataConnectionAdmin)
admin.site.register(MetaData, MetaDataAdmin)


