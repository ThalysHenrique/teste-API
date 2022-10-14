import imgleft
from imgleft.serializers import ModelSerializer
from .models import Imgleft

class ImgleftSerializer(ModelSerializer):
    class Meta:
        model = Imgleft
        fields = '__all__'