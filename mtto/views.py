from wsgiref.validate import validator
from django.forms import TextInput
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CargoForm,DepaForm,EmplForm
from .models import Cargo,Departamento,Empleado
from .validaciones import validate_nombre
from django.core.exceptions import ValidationError

# Create your views here.

def inicio(request):
    #return HttpResponse("BIenvenido a mi sitio")
    return render(request, "inicio.html")

def crearCargo(request):
    if request.method=="POST":
        cargo_form=CargoForm(request.POST)
        if cargo_form.is_valid():
            cargo_form.save()
            return redirect('listcargo')
    cargo_form=CargoForm()
    cargos=Cargo.objects.all()
    return render(request,"pages/cargo.html",{'cargoForm':cargo_form, 'cargos':cargos, 'accion':'Registrar'})
def listcargo(request):
    cargo_form=CargoForm()
    cargos=Cargo.objects.all()

    return render(request, "pages/listcargo.html",{'cargoForm':cargo_form, 'cargos':cargos})

def editarCargo(request,id):
    error,cargo_form=None,None
    try:
        cargo=Cargo.objects.get(id=id)
        if request.method=="GET":
            cargo_form=CargoForm(instance=cargo)
        else:
            cargo_form=CargoForm(request.POST,instance=cargo)
            if cargo_form.is_valid():
                cargo_form.save()
                return redirect('listcargo')
    except Exception as e:
        error=e
    cargos=Cargo.objects.all()
    return render(request,"pages/cargo.html",{'cargoForm':cargo_form, 'cargos':cargos, 'accion':'Modificar'})

def eliminarCargo(request,id):
    cargo=Cargo.objects.get(id=id)
    if request.method=='POST':
        cargo.delete()
        return redirect("listcargo")
    return render(request,"pages/eliminar_cargo.html",{'cargo':cargo})

def crearDepartamento(request):
    if request.method=="POST":
        depa_form=DepaForm(request.POST)
        if depa_form.is_valid():
            depa_form.save()
            return redirect('listdepa')
    depa_form=DepaForm()
    dptos=Departamento.objects.all()
    return render(request,"pages/departamento.html",{'depaForm':depa_form, 'departamentos':dptos, 'accion':'Registrar'})

def listdepa(request):
    depa_form=DepaForm()
    dptos=Departamento.objects.all()
    return render(request,"pages/listdepa.html",{'depaForm':depa_form, 'departamentos':dptos})

def editarDepa(request,id):
    error,depa_form=None,None
    try:
        departamento=Departamento.objects.get(id=id)
        if request.method=="GET":
            depa_form=DepaForm(instance=departamento)
        else:
            depa_form=DepaForm(request.POST,instance=departamento)
            if depa_form.is_valid():
                depa_form.save()
                return redirect('listdepa')
    except Exception as e:
        error=e
    dptos=Departamento.objects.all()
    return render(request,"pages/departamento.html",{'depaForm':depa_form, 'departamentos':dptos, 'accion':'Modificar'})

def eliminarDepa(request,id):
    departamento=Departamento.objects.get(id=id)
    if request.method=='POST':
        departamento.delete()
        return redirect("listdepa")
    return render(request,"pages/eliminar_depa.html",{'departamento':departamento})

def crearEmpleado(request):
    if request.method=="POST":
        empl_form=EmplForm(request.POST)
        if empl_form.is_valid():
            empl_form.save()
            return redirect('listempl')
    empl_form=EmplForm()
    emplds=Empleado.objects.all()
    return render(request,"pages/empleado.html",{'emplForm':empl_form, 'empleados':emplds, 'accion':'Registrar'})

def listempl(request):
    empl_form=EmplForm()
    emplds=Empleado.objects.all()
    return render(request,"pages/listempl.html",{'emplForm':empl_form, 'empleados':emplds, 'accion':'Registrar'})

def editarEmpl(request,id):
    error,empl_form=None,None
    try:
        empleado=Empleado.objects.get(codigo=id)
        if request.method=="GET":
            empl_form=EmplForm(instance=empleado)
        else:
            empl_form=EmplForm(request.POST,instance=empleado)
            if empl_form.is_valid():
                empl_form.save()
                return redirect('listempl')
    except Exception as e:
        error=e
    emplds=Empleado.objects.all()
    return render(request,"pages/empleado.html",{'emplForm':empl_form, 'empleados':emplds, 'accion':'Modificar'})

def eliminarEmpl(request,id):
    empleado=Empleado.objects.get(codigo=id)
    if request.method=='POST':
        empleado.delete()
        return redirect("listempl")
    return render(request,"pages/eliminar_empl.html",{'empleado':empleado})