from django.db import models

# Create your models here.

class Region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    nombreRegion = models.CharField(max_length=50, verbose_name='Región')

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regiones'

    def __str__(self):
        return self.nombreRegion


class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True)
    nombreComuna = models.CharField(max_length=50, verbose_name='Comuna')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'

    def __str__(self):
        return self.nombreComuna


class TipoProducto(models.Model):
    idTipoProducto = models.AutoField(primary_key=True)
    nombreTipoProducto = models.CharField(max_length=50, verbose_name='Nombre tipo producto')

    class Meta:
        verbose_name = 'Tipo de producto'
        verbose_name_plural = 'Tipo de productos'

    def __str__(self):
        return self.nombreTipoProducto


class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=100, verbose_name='Nombre producto')
    descripcion = models.CharField(max_length=300, verbose_name='Descripción')
    precio = models.IntegerField(verbose_name='Precio')
    imagen = models.ImageField(upload_to='proveedores', null=True, blank=True,verbose_name='Imagen')
    tipoProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombreProducto

class Proveedor(models.Model):
    idProveedor = models.AutoField(primary_key=True)
    nombreProveedor  = models.CharField(max_length=50, verbose_name='Nombre de la empresa')
    telefono = models.IntegerField(verbose_name='Número de telefono')
    correoElectronico = models.CharField(max_length=100, verbose_name='Correo electronico')
    direccion = models.CharField(max_length=120, verbose_name='Dirección')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto, verbose_name='Productos')

    class Meta:
        verbose_name = 'Proveedor' 
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombreProveedor