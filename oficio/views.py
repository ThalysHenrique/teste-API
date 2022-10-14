from rest_framework.viewsets import ModelViewSet
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.views import APIView, Response
from oficio.serializers import OficioSerializer
from .models import Oficio

# Create your views here.

class OficioViewSet(ModelViewSet):
    queryset = Oficio.objects.all()
    serializer_class = OficioSerializer
