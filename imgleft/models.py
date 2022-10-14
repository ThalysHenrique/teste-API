from django.db import models

# Create your models here.

class Imgleft(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)