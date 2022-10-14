from django.db import models

class Paragrafo1(models.Model):
    text = models.CharField(max_length=255)