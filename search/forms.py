from django import forms

from .models import SearchTerm

from accounts.models import UserProfile

from skills.models import CreditOptions

from skills.crew import CREWS

class SearchForm(forms.ModelForm):
    q = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Keyword(s) search'}))
    crew_position = forms.ChoiceField(choices=CREWS)
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City'}))
    project_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Production Name'}))
    affiliation = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Union/Guild'}))


    class Meta:
        model = SearchTerm