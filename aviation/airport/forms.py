from django import forms
from .models import Airport

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['airport_id','airport_name','airport_type','latitude','longitude','elevation','continent','country','municipality']
        # Defines the fields to be included in the form