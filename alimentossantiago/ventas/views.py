from django.shortcuts import render
from .models import ProductoPublico
from .forms import ItemCarritoForm

# Create your views here.


def carrito(request):
    return render(request, 'ventas/carrito.html')


def vista_productos_publicos(request):
    productos = ProductoPublico.objects.all()

    data = {
        'productos': productos,
        'form': ItemCarritoForm
    }

    if request.method == 'POST':
        formulario = ItemCarritoForm(request.POST)
        if formulario.is_valid():
            formulario.save()

    return render(request, 'ventas/productos_publicos.html', data)