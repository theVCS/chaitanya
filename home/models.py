from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.


class Gallery(models.Model):
    img = models.ImageField(upload_to="static/media/gallery/")
    time = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return str(self.pk)

    @classmethod
    def create(cls, img):
        gallery = cls(img=img)
        return gallery
