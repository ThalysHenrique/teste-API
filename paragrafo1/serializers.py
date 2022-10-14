from rest_framework.serializers import ModelSerializer
from .models import Paragrafo1

class Paragrafo1Serializer(ModelSerializer):
    class Meta:
        model = Paragrafo1
        fields = '__all__'