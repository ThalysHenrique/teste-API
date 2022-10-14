from django.db import models
from cabecalho.models import Cabecalho
from paragrafo1.models import Paragrafo1
from paragrafo2.models import Paragrafo2
from rodape.models import Rodape

class Oficio(models.Model):
    cabecalho = models.ManyToManyField(Cabecalho)
    paragrafo1 = models.ManyToManyField(Paragrafo1)
    paragrafo2 = models.ManyToManyField(Paragrafo2)
    rodape = models.ManyToManyField(Rodape)


    def __str__(self):
        return self.cabecalho
    