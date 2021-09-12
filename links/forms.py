from django import forms
from django.db import models
from .models import Link

class AddLinkForm(forms.ModelForm):
    
    class Meta:
        model = Link
        fields= ['url']
        