from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from upload.models import UploadedImage
from .forms import *

# Create your views here.
def index(request):
    alert_message = False
    if request.method == 'POST': 
        submitted_form = UploadImageForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            submitted_form.save()
            alert_message = {
                'status': True,
                'message': 'Successfully saved the image'
            }
        else:
            alert_message = {
                'status': False,
                'message': 'Form data is invalid. Please check if your image / title is repeated'
            }
    
    form = UploadImageForm()
    context = {
        'alert_data': alert_message,
        'form': form,
        'images': UploadedImage.objects.all
    }
    return render(request, 'index.html', context=context)