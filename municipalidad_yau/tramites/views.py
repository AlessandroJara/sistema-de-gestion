from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Tramite, Ciudadano
from .serializers import TramiteSerializer, CiudadanoSerializer

class CiudadanoViewSet(viewsets.ModelViewSet):
    queryset = Ciudadano.objects.all()
    serializer_class = CiudadanoSerializer
    permission_classes = [IsAuthenticated]

class TramiteViewSet(viewsets.ModelViewSet):
    queryset = Tramite.objects.all()
    serializer_class = TramiteSerializer
    permission_classes = [IsAuthenticated]