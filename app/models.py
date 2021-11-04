from django.db import models
import datetime as dt
from django.urls import reverse


# cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{ self.name }"
