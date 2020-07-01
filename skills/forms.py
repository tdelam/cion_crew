from django import forms
from django.contrib.auth.models import User
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.forms.models import BaseModelFormSet

from ckeditor.widgets import CKEditorWidget

from .models import CreditOptions, Skills

class SkillsForm(forms.ModelForm):
    available_as = forms.CharField(widget=CKEditorWidget(attrs={'maxlength': 100}), 
        help_text='(Optional) notes on what you are looking for.', required=False)
    weblink_1_description = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'e.g. IMDB Page'}))
    weblink_2_description = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'e.g. Twitter Page'}))
    weblink_3_description = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'e.g. Facebook Page'}))

    class Meta:
        model = Skills
        exclude = ('user',)


class BaseCreditFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseCreditFormSet, self).__init__(*args, **kwargs)
        self.extra = 0
        #self.queryset = CreditOptions.objects.filter(user=user) 

class CreditOptionsForm(forms.ModelForm):   
    class Meta:
        model = CreditOptions
        exclude = ('user',)

OptionFormset = formset_factory(CreditOptionsForm, extra=1)