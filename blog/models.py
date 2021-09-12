from os import rename
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.


class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=50, verbose_name='Heading')
    details = models.TextField(verbose_name="Details")
    img = models.ImageField(upload_to="static/media/blogs/")
    time = models.DateTimeField(default=datetime.now)
    commentsCnt = models.IntegerField(verbose_name="Comments Count",default=0)

    def __str__(self):
        return self.heading

    @classmethod
    def create(cls, owner, heading, details, img, time):
        blog = cls(owner=owner, heading=heading, details=details,
                   img=img, time=time)
        return blog


class Comment(models.Model):
    blogId = models.ForeignKey(Blog, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    details = models.TextField(verbose_name="Details")
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.details

    @classmethod
    def create(cls, blogId, owner, details):
        comment = cls(blogId=blogId, owner=owner, details=details)
        return comment
