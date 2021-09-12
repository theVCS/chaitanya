from os import rename
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.


class Contest(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=50, verbose_name='Heading')
    details = models.TextField(verbose_name="Details")
    img = models.ImageField(upload_to="static/media/contests")
    time = models.DateTimeField(default=datetime.now)
    commentsCnt = models.IntegerField(verbose_name="Comments Count",default=0)
    result = models.FileField(upload_to="static/media/result", blank=True, null=True)

    def __str__(self):
        return self.heading

    @classmethod
    def create(cls, owner, heading, details, img, time):
        contest = cls(owner=owner, heading=heading, details=details,
                   img=img, time=time)
        return contest


class Comment(models.Model):
    contestId = models.ForeignKey(Contest, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentOwner")
    details = models.TextField(verbose_name="Comment Details")
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.details

    @classmethod
    def create(cls, contestId, owner, details):
        comment = cls(contestId=contestId, owner=owner, details=details)
        return comment
