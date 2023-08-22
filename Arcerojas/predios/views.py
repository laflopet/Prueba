from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Predio, Propietario

# Create your views here.
def list_data(request):
    tipos_identificacion = Propietario.TIPOS_IDENTIFICACION
    context = {'tipos_identificacion': tipos_identificacion}
    tipo_propietario = Propietario.TIPOS_PROPIETARIO
    tipo_prop = {'tipo_propietario': tipo_propietario}
    tipo_predio= Predio.TIPOS_PREDIO
    tipo_pred = {'tipo_predio': tipo_predio}
    propietarios = Propietario.objects.all()
    predios = Predio.objects.all()
    
    context_1 = {
        'propietarios': propietarios,
        'predios': predios,
    }
    combine_dic = {**context, **tipo_prop, **tipo_pred, **context_1}
    
    return render(request, 'index.html', combine_dic)

def create_owner(request):
    if request.method == 'POST':
        propietario = Propietario(nombre=request.POST['nombre'], tipo=request.POST['tipo'], numero_identificacion=request.POST['numero_identificacion'], tipo_identificacion=request.POST['tipo_identificacion'])
        propietario.save()
        return redirect('index')
        #return redirect('list_data')
    
def create_predio(request):
    if request.method == 'POST':
        predio = Predio(nombre_direccion=request.POST['nombre_direccion'], tipo_predio=request.POST['tipo_predio'], numero_catastral=request.POST['numero_catastral'], numero_matricula_inmobiliaria=request.POST['numero_matricula'])
        predio.save()
        return redirect('index')

# def editar_predio(request, id_predio):
#     predio = get_object_or_404(Predio, id=id_predio)

#     if request.method == 'POST':
#         # Obtener los nuevos datos desde el POST
#         nuevo_nombre_direccion = request.POST['nuevo_nombre_direccion']
#         nuevo_tipo_predio = request.POST['nuevo_tipo_predio']
#         nuevo_numero_catastral = request.POST['nuevo_numero_catastral']
#         nuevo_numero_matricula = request.POST['nuevo_numero_matricula']

#         # Actualizar los atributos del predio
#         predio.nombre_direccion = nuevo_nombre_direccion
#         predio.tipo_predio = nuevo_tipo_predio
#         predio.numero_catastral = nuevo_numero_catastral
#         predio.numero_matricula_inmobiliaria = nuevo_numero_matricula
#         predio.save()

#         return redirect('index')

def eliminar_predio(request, id_predio):
    eliminar_predio = Predio.objects.get(id=id_predio)
    eliminar_predio.delete()  
    return redirect('index')
