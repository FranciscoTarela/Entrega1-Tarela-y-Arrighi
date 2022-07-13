from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('familiar/', familiar, name='familiar'),
    path('autos/', autos, name='autos'),
    path('mascotas/', mascotas, name='mascotas'),
    path('familiarFormulario/', familiarFormulario, name='familiarFormulario'),
    path('autosFormulario/', autosFormulario, name='autosFormulario'),
    path('mascotaFormulario/', mascotaFormulario, name='mascotaFormulario'),
    path('busquedaAuto/', busquedaAuto, name='busquedaAuto'),
    path('buscarauto/', buscarauto, name='buscarauto'),
    path('busquedaMascota/', busquedaMascota, name='busquedaMascota'),
    path('buscarmascota/', buscarmascota, name='buscarmascota'),
    path('busquedaFamiliar/', busquedaFamiliar, name='busquedaFamiliar'),
    path('buscarfamiliar/', buscarfamiliar, name='buscarfamiliar'),
    ]