from django import forms

class FamiliarForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.IntegerField()
    fecha = forms.DateField() 

class autosForm(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    fecha_fabricacion = forms.IntegerField()

class mascotaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    raza = forms.CharField(max_length=50)
