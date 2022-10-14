from django.db import models

class Paragrafo2(models.Model):
    text = models.CharField(max_length=255)