from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def vista_proveedores(request):
    proveedor = Proveedor.objects.all()
    datos = {
        'proveedor' : proveedor
    }
    return render(request, 'proveedores/proveedor.html', datos)

def vista_productos(request, id):
    productos = Proveedor.objects.filter(idProveedor=id)

    data = {
        'productos': productos
    }
    return render(request, 'proveedores/productos.html', data)
