from django.db.models.base import Model
from rest_framework import fields, serializers
from rayoapp.models import Vehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'anio', 'color', 'cliente']