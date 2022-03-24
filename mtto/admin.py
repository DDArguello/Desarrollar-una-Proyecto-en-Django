from django.contrib import admin
from .models import Cargo, Departamento, Empleado

# Register your models here.

admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(Empleado)