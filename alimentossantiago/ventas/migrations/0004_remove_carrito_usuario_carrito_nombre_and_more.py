# Generated by Django 4.0.1 on 2022-06-15 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_productopublico_imagen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='usuario',
        ),
        migrations.AddField(
            model_name='carrito',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='totalCarrito',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total'),
        ),
    ]
