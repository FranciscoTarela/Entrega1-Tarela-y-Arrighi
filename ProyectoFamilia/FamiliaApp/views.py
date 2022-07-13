from django.shortcuts import render
from FamiliaApp.models import Familiar, Auto, Mascota
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from FamiliaApp.forms import FamiliarForm, autosForm, mascotaForm
# Create your views here.

#ignorar esta funcion, era del proyecto pasado"
'''def familiares(request):
    familiares = Familiar(nombre='Daniel', apellido='Paredes', dni=3874846, fecha="1968-07-12")
    texto=f"<br>Familiar Agregado {familiares.nombre} {familiares.apellido} DNI: {familiares.dni} Fecha de Nacimiento: {familiares.fecha}</br>\n"
    familiares = Familiar(nombre='Myriam',apellido='Arrighi', dni=16840508, fecha="1965-09-20")
    texto+=f"<br>Familiar Agregado {familiares.nombre} {familiares.apellido} DNI: {familiares.dni} Fecha de Nacimiento: {familiares.fecha}</br>\n"
    familiares = Familiar(nombre='Santina',apellido='Molinari',dni=10180457, fecha="1945-06-20")
    texto+=f"<br>Familiar Agregado {familiares.nombre} {familiares.apellido} DNI: {familiares.dni} Fecha de Nacimiento: {familiares.fecha}</br>\n"
    familiares.save()

    html= open("E:/NuevoProyecto/ProyectoFamilia/FamiliaApp/templates/template.html")

    plantilla= Template(html.read())

    html.close()

    micontexto = Context(familiares)

    texto+=plantilla.render (micontexto)

    return HttpResponse (texto)'''

def inicio(request):
    return render(request, "FamiliaApp/inicio.html")

def autos(request):
    return render(request, "FamiliaApp/autos.html")

def mascotas(request):
    return render(request, "FamiliaApp/mascota.html")

def familiar(request):
    return render(request, "FamiliaApp/familiar.html")

def familiarFormulario(request):
    if (request.method=="POST"):
        form = FamiliarForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            dni = info["dni"]
            fecha = info["fecha"]
            familiar = Familiar(nombre=nombre, apellido=apellido, dni=dni, fecha=fecha)
            familiar.save()
            return render(request, "FamiliaApp/inicio.html")
    else:
        form = FamiliarForm()
    return render(request, "FamiliaApp/familiarFormulario.html", {"form":form})
        
def autosFormulario(request):
    if (request.method=="POST"):
        form = autosForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            marca = info["marca"]
            modelo = info["modelo"]
            fecha_fabricacion = info["fecha_fabricacion"]
            auto = Auto(marca=marca, modelo=modelo, fecha_fabricacion=fecha_fabricacion)
            auto.save()
            return render(request, "FamiliaApp/inicio.html")
    else:
        form = autosForm()
    return render(request, "FamiliaApp/autosFormulario.html", {"form":form})

def mascotaFormulario(request):
    if (request.method=="POST"):
        form = mascotaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            raza = info["raza"]
            edad = info["edad"]
            mascota = Mascota(nombre=nombre, raza=raza, edad=edad)
            mascota.save()
            return render(request, "FamiliaApp/inicio.html")
    else:
        form = mascotaForm()
    return render(request, "FamiliaApp/mascotaFormulario.html", {"form":form})

def busquedaFamiliar(request):
    return render(request, "FamiliaApp/busquedaFamiliar.html")

def busquedaMascota(request):
    return render(request, "FamiliaApp/busquedaMascota.html")

def busquedaAuto(request):
    return render(request, "FamiliaApp/busquedaAuto.html")

def buscarauto(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        autos = Auto.objects.filter(marca=marca)
        return render(request, "FamiliaApp/resultadosBusquedaAutos.html", {"autos":autos})
    else:
        return render(request, "FamiliaApp/busquedaAuto.html", {"error":"No se ingreso ninguna marca"})
    
def buscarmascota(request):
    if request.GET["raza"]:
        raza = request.GET["raza"]
        mascotas = Mascota.objects.filter(raza=raza)
        return render(request, "FamiliaApp/resultadosBusquedaMascota.html", {"mascotas":mascotas})
    else:
        return render(request, "FamiliaApp/busquedaMascota.html", {"error": "No se ingreso ninguna raza"})

def buscarfamiliar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        familiares = Familiar.objects.filter(nombre=nombre)
        return render(request, "FamiliaApp/resultadosBusquedaFamiliar.html", {"familiares":familiares})
    else:
        return render(request, "FamiliaApp/busquedaFamiliar.html", {"error": "No se ingreso ningun familiar"})


