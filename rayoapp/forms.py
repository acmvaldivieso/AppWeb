from django import forms
from django.forms import ModelForm
from .models import Vehiculo, Cliente

class VehiculoForm(ModelForm):
    class Meta: 
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'anio', 'color', 'cliente']

class ClienteForm(ModelForm):
    class Meta: 
        model = Cliente
        fields = ['rut_cliente', 'pnombre', 'apaterno', 'amaterno', 'email', 'telefono']
