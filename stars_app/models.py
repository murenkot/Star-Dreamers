from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Photo(models.Model):
    date = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    explanation = models.TextField()
    url = models.TextField()
    hdurl = models.TextField()


