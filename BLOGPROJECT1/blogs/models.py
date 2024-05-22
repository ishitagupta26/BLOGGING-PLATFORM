from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class blogs(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


class User(models.Model):
     username = models.CharField(max_length=30)
     password = models.CharField(max_length=30)
     email = models.EmailField()