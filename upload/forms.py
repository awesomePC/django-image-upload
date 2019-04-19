from django import forms 
from .models import *
  
class UploadImageForm(forms.ModelForm): 
  
    class Meta: 
        model = UploadedImage 
        fields = ['image', 'title'] 