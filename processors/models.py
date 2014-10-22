from django.db import models
import processors.helpers as processingfuncs
from django.utils.translation import ugettext_lazy as _




class Processor(models.Model):

    #this will be populoated from the enumerations field
    title = models.CharField('Processor Name', max_length=300, help_text=_('Name of the indicator'), unique=True)

    def run(self):
        #call function from string
        methodToCall = getattr(processingfuncs, self.title)
        result = methodToCall()




