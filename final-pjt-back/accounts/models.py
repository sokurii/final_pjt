from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    gender = models.TextField()
    age = models.TextField()
    residence = models.TextField()