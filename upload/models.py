from django.db import models
import uuid

# Create your models here.
class UploadedImage(models.Model):
    title = models.CharField(primary_key=True, max_length=100, help_text='Enter an image title')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title