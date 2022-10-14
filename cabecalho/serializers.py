from pyexpat import model
from oficio import serializers
from imagem_cabecalho.serializers import ModelSerializer
from .models import Cabecalho

class CabecalhoSerializer(ModelSerializer):
    class Meta:
        model = Cabecalho
        fields = '__all__'