from rest_framework import serializers
from .models import Curriculum

class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ['id', 'ciudadano', 'archivo', 'metadata', 'puntuacion', 'fecha_subida']