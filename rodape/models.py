from django.db import models

# Create your models here.

class Rodape(models.Model):
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=32) 
    email = models.EmailField()
    imgleft = models.OneToOneField("imgleft.imgleft", on_delete=models.DO_NOTHING,related_name='imgleft')
    imgright = models.OneToOneField("imgright.imgright", on_delete=models.DO_NOTHING,related_name='imgrigth')
