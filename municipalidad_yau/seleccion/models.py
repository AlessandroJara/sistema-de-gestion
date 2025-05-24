from django.db import models
from tramites.models import Ciudadano

class Curriculum(models.Model):
    ciudadano = models.ForeignKey(Ciudadano, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='curriculos/')  # PDF
    metadata = models.JSONField()  # Educación, experiencia, habilidades
    puntuacion = models.FloatField(default=0.0)  # Calculada por ML
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Currículo de {self.ciudadano.nombre}"