from django.urls import path
from .views import *

urlpatterns = [
    path('', vista_productos_publicos, name='vista_productos_publicos'),
    path('carrito/', carrito, name='carrito'),
    
]