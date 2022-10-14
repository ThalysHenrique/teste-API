from rest_framework.serializers import ModelSerializer
from .models import Imgright

class ImgrigthSerializer(ModelSerializer):
    class Meta:
        model = Imgright
        fields = '__all__'