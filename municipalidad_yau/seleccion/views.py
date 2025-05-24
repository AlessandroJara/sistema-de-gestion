from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Curriculum
from .serializers import CurriculumSerializer

class CurriculumViewSet(viewsets.ModelViewSet):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
    permission_classes = [IsAuthenticated]