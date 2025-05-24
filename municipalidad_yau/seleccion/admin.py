from django.contrib import admin
from .models import Curriculum

@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ['ciudadano', 'fecha_subida', 'puntuacion']
    search_fields = ['ciudadano__nombre']