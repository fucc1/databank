# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MetaData'
        db.create_table(u'etldata_metadata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('contactpoint', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('contactemail', self.gf('django.db.models.fields.EmailField')(max_length=255, blank=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('bureauCode', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('programCode', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('accessLevelComment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('license', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spatial', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('temporal', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'etldata', ['MetaData'])

        # Adding model 'DataConnection'
        db.create_table(u'etldata_dataconnection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('indicator', self.gf('django.db.models.fields.CharField')(unique=True, max_length=300)),
            ('sectorid', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('agency', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('metadataURL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('update_freq', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('raw_response', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('orgURL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('webservice', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('technicalnotes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('units', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('metadata', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['etldata.MetaData'], null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sector', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('downloadedFile', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('preprocessors', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['processors.Processor'], null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='Not Checked', max_length=255)),
        ))
        db.send_create_signal(u'etldata', ['DataConnection'])


    def backwards(self, orm):
        # Deleting model 'MetaData'
        db.delete_table(u'etldata_metadata')

        # Deleting model 'DataConnection'
        db.delete_table(u'etldata_dataconnection')


    models = {
        u'etldata.dataconnection': {
            'Meta': {'object_name': 'DataConnection'},
            'agency': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
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