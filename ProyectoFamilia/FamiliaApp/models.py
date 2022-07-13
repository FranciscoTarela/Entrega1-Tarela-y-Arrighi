from django.db import models
from datetime import datetime, date

class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre+" "+str(self.apellido)+" "+str(self.dni)+" "+str(self.fecha)

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    raza = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+str(self.edad)+" "+str(self.raza)

class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    fecha_fabricacion = models.IntegerField()

    def __str__(self):
        return self.marca+" "+str(self.modelo)+" "+str(self.fecha_fabricacion)