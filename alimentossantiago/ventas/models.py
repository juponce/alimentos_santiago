from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class CarritoCompra(models.Model):
class Carrito(models.Model):
    idCarrito = models.AutoField(primary_key=True)
    totalCarrito = models.IntegerField(verbose_name='Total', null=True, blank=True)
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', null=True, blank=True)

    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'

    def __str__(self):
        return self.idCarrito


class Descuento(models.Model):
    idDescuento = models.AutoField(primary_key=True)
    nombreDescuento = models.CharField(max_length=100, verbose_name='Nombre descuento')
    descripcion = models.CharField(max_length=254, verbose_name='Descripción descuento')
    porcentajeDescuento = models.IntegerField(verbose_name='porcentajeDescuento')
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fechaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Descuento'
        verbose_name_plural = 'Descuentos'

    def __str__(self):
        return self.nombreDescuento


class CategoriaProducto(models.Model):
    idCategoriaProducto = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=100, verbose_name='Nombre categoria')

    class Meta:
        verbose_name = 'Categoria producto'
        verbose_name_plural = 'Categorias productos'

    def __str__(self):
        return self.nombreCategoria


class ProductoPublico(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=100, verbose_name='Nombre del producto')
    descripcion = models.CharField(max_length=254, verbose_name='Descripción')
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    precio = models.IntegerField(verbose_name='Precio')
    descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE, null=True, blank=True)
    stock = models.IntegerField(verbose_name='Stock disponible')
    imagen = models.ImageField(upload_to='ventas', null=True, blank=True,verbose_name='Imagen')
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fechaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Producto Publico'
        verbose_name_plural = 'Productos Publicos'
    
    def __str__(self):
        return self.nombreProducto


class ItemCarrito(models.Model):
    idItemCarrito = models.AutoField(primary_key=True)
    cantidad  = models.IntegerField(verbose_name='Cantidad')
    producto = models.ForeignKey(ProductoPublico, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item del carrito'
        verbose_name_plural = 'Items del carrito'
    
    def __str__(self):
        return self.idItemCarrito


class DetallePedido(models.Model):
    idDetallePedido = models.AutoField(primary_key=True)
    total = models.ImageField(verbose_name='Total pedido')
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fechaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


class ItemsPedido(models.Model):
    idItemsPedido = models.AutoField(primary_key=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fechaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    producto = models.ForeignKey(ProductoPublico, on_delete=models.CASCADE)
    detallePedido = models.ForeignKey(DetallePedido, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item del pedido'
        verbose_name_plural = 'Items del pedido'
    
    def __str__(self):
        return self.idItemsPedido