from django.db import models
from django.contrib.auth.models import User

class Ciudadano(models.Model):
    dni = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Tramite(models.Model):
    ESTADOS = (
        ('PENDIENTE', 'Pendiente'),
        ('EN_REVISION', 'En Revisión'),
        ('APROBADO', 'Aprobado'),
        ('RECHAZADO', 'Rechazado'),
    )
    TIPO_TRAMITE = (
        ('LICENCIA', 'Licencia de Construcción'),
        ('PERMISO', 'Permiso de Funcionamiento'),
        ('SERVICIO', 'Servicio Público'),
    )
    ciudadano = models.ForeignKey(Ciudadano, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=TIPO_TRAMITE)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    documentos = models.JSONField()  # Almacena metadatos de documentos
    prioridad = models.FloatField(default=0.0)  # Calculada por ML
    errores = models.TextField(blank=True)  # Errores detectados

    def __str__(self):
        return f"{self.tipo} - {self.estado}"