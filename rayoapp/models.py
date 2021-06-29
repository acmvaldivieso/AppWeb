from django.db import models
from django.db.models.manager import ManagerDescriptor

# Create your models here.
class Cliente(models.Model):
    rut_cliente = models.IntegerField (primary_key=True, verbose_name='Rut')
    pnombre = models.CharField(max_length=30, verbose_name='Primer nombre')
    apaterno = models.CharField(max_length=30, verbose_name='Apellido Paterno')
    amaterno = models.CharField(max_length=30, verbose_name='Apellido Materno', null=True,)
    email = models.CharField(max_length=50, verbose_name='Email')
    telefono = models.IntegerField(verbose_name='Telefono')

    def __str__(self):
        return '%s / %s %s %s' % (self.rut_cliente, self.pnombre, self.apaterno, self.amaterno)
    
class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=10, verbose_name='Patente')
    marca = models.CharField(max_length=30, blank=True, verbose_name='Marca')
    modelo = models.CharField(max_length=50, blank=True, verbose_name='Modelo')
    anio = models.IntegerField(verbose_name='Año')
    color = models.CharField(max_length=30, blank=True ,verbose_name='Color')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return 'Vehiculo: %s - %s - %s - (%s)' % (self.marca, self.modelo, self.color, self.patente)
    
