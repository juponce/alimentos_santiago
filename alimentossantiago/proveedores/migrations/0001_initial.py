# Generated by Django 4.0.1 on 2022-06-06 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombreComuna', models.CharField(max_length=50, verbose_name='Comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=100, verbose_name='Nombre producto')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripción')),
                ('precio', models.IntegerField(verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False)),
                ('nombreRegion', models.CharField(max_length=50, verbose_name='Región')),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('idTipoProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombreTipoProducto', models.CharField(max_length=50, verbose_name='Nombre tipo producto')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idProveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProveedor', models.CharField(max_length=50, verbose_name='Nombre de la empresa')),
                ('telefono', models.IntegerField(verbose_name='Número de telefono')),
                ('correoElectronico', models.CharField(max_length=100, verbose_name='Correo electronico')),
                ('direccion', models.CharField(max_length=120, verbose_name='Dirección')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.comuna')),
                ('producto', models.ManyToManyField(to='proveedores.Producto', verbose_name='Productos')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tipoProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.tipoproducto'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.region'),
        ),
    ]
