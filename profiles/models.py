from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(
        blank=True, max_length=30, verbose_name='Last Name')
    email_id = models.EmailField(blank=True, verbose_name='Email ID')
    phone_number = models.CharField(max_length=12)
    resume = models.FileField(upload_to="resume")

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, user, first_name, last_name, email_id, phone_number,resume):
        profile = cls(user=user, first_name=first_name, last_name=last_name,
                      email_id=email_id, phone_number=phone_number,resume=resume)
        return profile
