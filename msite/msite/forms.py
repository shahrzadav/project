__author__ = 'ASTIAG'
from msiteapp.models import HomeWorks
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm


class ModelFormWithFileField(ModelForm):
    class Meta:
        model = HomeWorks
        fields = ('q_file', 'topic')

    #class Meta:
     #   error_messages = {
      #      NON_FIELD_ERRORS: {'unique_together': "%(model_name)s's %(field_labels)s are not unique.", }
       # }

