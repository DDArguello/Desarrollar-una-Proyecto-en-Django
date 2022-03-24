from dataclasses import field, fields
from http.client import ImproperConnectionState
from tkinter import Widget
from django import forms
from .models import Cargo,Departamento, Empleado

class CargoForm(forms.ModelForm):
    class Meta:
        model=Cargo
        fields=['descripcion','estado']
        widgets={'descripcion':forms.TextInput(attrs={
            'placeholder':'Ingrese un cargo',
            'class':'form-group',
            'required':True,
            
        }),
        }

class DepaForm(forms.ModelForm):
    class Meta:
        model=Departamento
        fields=['descripcion','estado']
        widgets={'descripcion':forms.TextInput(attrs={
            'placeholder':'Ingrese un departamento',
            'class':'form-group',
            'required':True
        })   
        }

class EmplForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=['nombre','cedula','cargo','departamento','sueldo','estado']
        widgets={'nombre':forms.TextInput(attrs={
            'placeholder':'Ingrese un nombre',
            'class':'form-group',
            'required':True
            }),
            'cedula':forms.TextInput(attrs={
            'placeholder':'Ingrese su cedula',
            'class':'form-group',
            'required':True
            }),
            'cargo':forms.Select(attrs={
            'placeholder':'Ingrese su cedula',
            'class':'form-group',
            'required':True
            }),
            'departamento':forms.Select(attrs={
            'placeholder':'Ingrese su cedula',
            'class':'form-group',
            'required':True
            }),
            'sueldo':forms.TextInput(attrs={
            'placeholder':'Ingrese su sueldo',
            'class':'form-group',
            'required':True})
            }
            