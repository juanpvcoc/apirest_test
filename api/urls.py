from django.urls import path, include
from api import views

# urlpatterns = [
#     path('', views.index, name="index"),
# ]

# Crear rutas de una API Rest con django rest_framework
from rest_framework import routers
from .api import ApiViewSet

ruta = routers.DefaultRouter()
ruta.register('empleados', ApiViewSet, 'api')

urlpatterns = ruta.urls