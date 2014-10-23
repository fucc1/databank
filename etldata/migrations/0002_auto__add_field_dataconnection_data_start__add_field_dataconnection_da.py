# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DataConnection.data_start'
        db.add_column(u'etldata_dataconnection', 'data_start',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DataConnection.data_end'
        db.add_column(u'etldata_dataconnection', 'data_end',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DataConnection.data_start'
        db.delete_column(u'etldata_dataconnection', 'data_start')

        # Deleting field 'DataConnection.data_end'
        db.delete_column(u'etldata_dataconnection', 'data_end')


    models = {
        u'etldata.dataconnection': {
            'Meta': {'object_name': 'DataConnection'},
            'agency': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'data_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'downloadedFile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicator': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '300'}),
            'metadata': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['etldata.MetaData']", 'null': 'True', 'blank': 'True'}),
            'metadataURL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'orgURL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'preprocessors': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['processors.Processor']", 'null': 'True', 'blank': 'True'}),
            'raw_response': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sector': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sectorid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Not Checked'", 'max_length': '255'}),
            'technicalnotes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'units': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'update_freq': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'webservice': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'etldata.metadata': {
            'Meta': {'object_name': 'MetaData'},
            'accessLevelComment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bureauCode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contactemail': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'blank': 'True'}),
            'contactpoint': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'license': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'programCode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'spatial': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'temporal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'processors.processor': {
            'Meta': {'object_name': 'Processor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '300'})
        }
    }

    complete_apps = ['etldata']