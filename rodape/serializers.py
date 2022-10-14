from rest_framework.serializers import ModelSerializer
from imgleft.serializers import ImgleftSerializer
from imgright.serializers import ImgrigthSerializer
from rodape.models import Rodape

class RodapeSerializer(ModelSerializer):
    class Meta:
        model = Rodape
        fields = '__all__'
    
    
    #endereco = serializers.CharField(max_length=255)
    #telefone = serializers.CharField(max_length=32) 
    #email = serializers.EmailField()
    #imgleft = ImgleftSerializer()
    #imgright = ImgrigthSerializer()
    #