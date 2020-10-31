from django.contrib import admin
from django.urls import path, include
from .views import hindex,galeria,mision_vision,direccion,registro,login,logout_vista,registro_insumo,admin_insumos


urlpatterns = [
    path('',hindex,name='HINDEX'),
    path('galeria/',galeria,name='GALE'),
    path('mision/',mision_vision,name='MISION'),
    path('direccion/',direccion,name='UBICACION'),
    path('registro/',registro,name='FORMU'),
    path('login/',login,name='LOGIN'),
    path('logout_vista/',logout_vista,name='LOGOUT'),
    path('registro_insumo/',registro_insumo,name='INSUMOS'),
    path('admin_insumos/',admin_insumos,name='ADMIN'),
]


admin.site.site_header="Administración Lavado de Autos"