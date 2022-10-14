from django.db import models

class Cabecalho(models.Model):
    text = models.CharField(max_length=255)
    #img = models.OneToOneField("imagem_cabecalho.imagem_cabecalho", on_delete=models.DO_NOTHING)
    