from django.urls import path
from .views import *

urlpatterns = [
    path('', vista_proveedores, name='proveedores'),
    path('productos/<int:id>', vista_productos, name='productos'),
]