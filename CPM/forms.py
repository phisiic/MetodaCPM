from django import forms
from .models import Czynnosc, Zdarzenie, CPM

class CPMForm(forms.Form):
    no_activities = forms.IntegerField(label='No. of activities', min_value=2)
    no_events = forms.IntegerField(label='No. of events', min_value=2)
    file_name = forms.CharField(label='File name')

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Czynnosc
        fields = ('name', 'duration', 'before', 'after')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class CsvForm(forms.Form):
    file = forms.FileField(label='File')

