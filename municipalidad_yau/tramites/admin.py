from django.contrib import admin
from .models import Ciudadano, Tramite

@admin.register(Ciudadano)
class CiudadanoAdmin(admin.ModelAdmin):
    list_display = ['dni', 'nombre', 'email', 'telefono']
    search_fields = ['dni', 'nombre']

@admin.register(Tramite)
class TramiteAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'estado', 'ciudadano', 'fecha_solicitud', 'prioridad']
    list_filter = ['tipo', 'estado']
    search_fields = ['ciudadano__nombre']