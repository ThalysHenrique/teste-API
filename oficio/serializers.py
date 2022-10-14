from oficio.models import Oficio
from rest_framework.serializers import ModelSerializer

#from cabecalho.models import Cabecalho
#from paragrafo1.models import Paragrafo1
#from paragrafo2.models import Paragrafo2
#from rodape.models import Rodape

class OficioSerializer(ModelSerializer):
    class Meta:
        model = Oficio
        fields = '__all__'
    

    #cabecalho = CabecalhoSerializer(many=True)
    #paragrafo1 = Paragrafo1Serializer()
    #paragrafo2 = Paragrafo2Serializer()
    #rodape = RodapeSerializer(many=True)
