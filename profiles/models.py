from os import rename
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    firstName = models.CharField(max_length=30, verbose_name='First Name')
    lastName = models.CharField(blank=True, max_length=30, verbose_name='Last Name')
    email = models.EmailField(unique=True, verbose_name='Email ID')
    phone = models.CharField(max_length=13)
    resume = models.FileField(upload_to="media/resume")

    def __str__(self):
        return self.user.username

    @classmethod
    def create(cls, user, first_name, last_name, email_id, phone_number,resume):
        profile = cls(user=user, firstName=first_name, lastName=last_name,
                      email=email_id, phone=phone_number,resume=resume)
        return profile
