from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    label = models.CharField(max_length=16, null=True)
    author = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    likeCount = models.IntegerField
    dislikeCount = models.IntegerField
    commentCount = models.IntegerField
    rating = models.CharField(max_length=4, null=True)
    # content = models.CharField(max_length=4096)
    date = models.DateTimeField(auto_created=True, auto_now=True)
