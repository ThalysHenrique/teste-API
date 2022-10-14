from oficio import serializers
from imagem_cabecalho.serializers import ModelSerializer
from .models import Imagem_cabecalho

class Imagem_cabecalhoSerializer(ModelSerializer):
    class Meta:
        model = Imagem_cabecalho
        fields = '__all__'