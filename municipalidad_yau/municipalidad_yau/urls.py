from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tramites.views import TramiteViewSet, CiudadanoViewSet
from seleccion.views import CurriculumViewSet

router = DefaultRouter()
router.register(r'ciudadanos', CiudadanoViewSet)
router.register(r'tramites', TramiteViewSet)
router.register(r'curriculos', CurriculumViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
