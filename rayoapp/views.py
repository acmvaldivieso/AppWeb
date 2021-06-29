from django.shortcuts import render, redirect
from .models import Vehiculo, Cliente
from .forms import VehiculoForm, ClienteForm


# Create your views here.

def home(request):
    return render(request, 'rayoapp/index.html')

def contacto(request):
    return render(request, 'rayoapp/contacto.html')

def crear(request):
    return render(request, 'rayoapp/crear.html')

def mecanicos(request):
    return render(request, 'rayoapp/mecanicos.html')

def servicios(request):
    return render(request, 'rayoapp/servicios.html')

def formularios(request):
    return render(request, 'rayoapp/formularios.html')

def listar(request):
    ListaVehiculos = Vehiculo.objects.all()
    datos = {
        'vehiculos':ListaVehiculos,
    }
    return render(request, 'rayoapp/listar.html', datos)

def form_vehiculo(request):
    datos = {
        'form':VehiculoForm()
    }
    if(request.method == 'POST'):
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Datos Guardados Correctamente'
    return render(request, 'rayoapp/form_vehiculo.html', datos)

def form_cliente(request):
    datos = {
        'form':ClienteForm()
    }
    if(request.method == 'POST'):
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Datos Guardados Correctamente'
    return render(request, 'rayoapp/form_cliente.html', datos)

def form_mod_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    datos = {
        'form':VehiculoForm(instance=vehiculo)
    }

    if(request.method == 'POST'):
        formulario = VehiculoForm(data=request.POST, instance=vehiculo)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificado correctamente'

    return render(request,'rayoapp/form_mod_vehiculo.html',datos)


def form_del_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()

    return redirect(to='listar')
