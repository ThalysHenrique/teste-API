from rest_framework.serializers import ModelSerializer
from .models import Paragrafo2

class Paragrafo2Serializer(ModelSerializer):
    class Meta:
        model = Paragrafo2
        fields = '__all__'