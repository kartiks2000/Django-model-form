from django import forms
from formapp.models import stru

class myf(forms.ModelForm):
    
    class Meta:
        model = stru
        fields = ['first_name', 'last_name',]

    
