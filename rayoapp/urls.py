from django.urls import path
from .views import home, contacto, crear, mecanicos, servicios, listar, form_vehiculo, form_cliente, form_mod_vehiculo, form_del_vehiculo, formularios

urlpatterns = [
    path('', home, name='home'), 
    path('contacto', contacto, name='contacto'), 
    path('crear', crear, name='crear'), 
    path('mecanicos', mecanicos, name='mecanicos'), 
    path('servicios', servicios, name='servicios'), 
    path('listar', listar, name='listar'), 
    path('registrar_vehiculo', form_vehiculo, name='form_vehiculo'), 
    path('registrar_cliente', form_cliente, name='form_cliente'), 
    path('modificar_vehiculo/<id>', form_mod_vehiculo, name='form_mod_vehiculo'),
    path('eliminar_vehiculo/<id>',form_del_vehiculo,name='form_del_vehiculo'), 
    path('formularios', formularios, name='formularios'), 
]
 