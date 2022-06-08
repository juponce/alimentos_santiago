# Generated by Django 4.0.1 on 2022-06-08 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comuna',
            options={'verbose_name': 'Comuna', 'verbose_name_plural': 'Comunas'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Region', 'verbose_name_plural': 'Regiones'},
        ),
        migrations.AlterModelOptions(
            name='tipoproducto',
            options={'verbose_name': 'Tipo de producto', 'verbose_name_plural': 'Tipo de productos'},
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='proveedores', verbose_name='Imagen'),
        ),
    ]
