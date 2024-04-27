from django.db import models

# Create your models here.
class Empleados(models.Model):
    identificacion = models.CharField(max_length=12)
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    correo = models.CharField(max_length=128)
    salario_base = models.IntegerField()
    activo = models.BooleanField(default=True)