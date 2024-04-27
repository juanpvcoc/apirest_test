from .models import Empleados
from rest_framework import serializers

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = ('id', 'identificacion', 'nombres', 'apellidos', 'correo', 'salario_base', 'activo')

        # read_only_fields = ('id',) # Se agrega la "," para que sea detectado como una tupla