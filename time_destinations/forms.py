from django import forms
from .models import TimeDestination

class TimeDestinationform(forms.ModelForm):
    class Meta:
        model = TimeDestination
        fields = ['name', 'description', 'origin', 'destination']