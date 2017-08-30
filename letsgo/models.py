#from __future__ import unicode_literals

#from django.db import models

# Create your models here.

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.

#fs = FileSystemStorage(location = '/media/photos')
class Event(models.Model):
    name = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    time = models.TimeField(null = True)
    date = models.DateField(null = True)
    blurb = models.TextField()
    description = models.TextField()
    categories = models.TextField()
    location = models.TextField()
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    #photo = models.ImageField(upload_to = '/Users/Kriti/createathon/letsgo/media', blank = True)
    photo = models.ImageField()

    @property
    def photo_url(self):
    	if self.photo and hasattr(self.photo, 'url'):
            return "/".join(self.photo.url.split("/")[-2:])
