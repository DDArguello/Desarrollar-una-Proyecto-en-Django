"""nomina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mtto.views import crearDepartamento,editarCargo,eliminarCargo,editarDepa,eliminarDepa,crearEmpleado,editarEmpl,eliminarEmpl
from mtto.views import inicio,crearCargo,listcargo,listdepa,listempl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="inicio"),
    path('cargo/',crearCargo,name="cargo"),
    path('dpto/',crearDepartamento,name="departamento"),
    path('empleado/',crearEmpleado,name="empleado"),
    path('editarEmpl/<int:id>',editarEmpl,name="editarEmpl"),
    path('editarCargo/<int:id>',editarCargo,name="editarCargo"),
    path('eliminarCargo/<int:id>',eliminarCargo,name="eliminarCargo"),
    path('editarDepa/<int:id>',editarDepa,name="editarDepa"),
    path('eliminarDepa/<int:id>',eliminarDepa,name="eliminarDepa"),
    path('eliminarEmpl/<int:id>',eliminarEmpl,name="eliminarEmpl"),
    path('listcargo/',listcargo,name="listcargo"),
    path('listdepa/',listdepa,name="listdepa"),
    path('listempl/',listempl,name="listempl"),
]
