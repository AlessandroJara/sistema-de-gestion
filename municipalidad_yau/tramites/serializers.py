from rest_framework import serializers
from .models import Tramite, Ciudadano

class CiudadanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudadano
        fields = ['id', 'dni', 'nombre', 'email', 'telefono']

class TramiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tramite
        fields = ['id', 'ciudadano', 'tipo', 'estado', 'fecha_solicitud', 'documentos', 'prioridad', 'errores']