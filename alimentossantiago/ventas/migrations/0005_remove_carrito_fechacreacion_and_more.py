# Generated by Django 4.0.1 on 2022-06-16 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_remove_carrito_usuario_carrito_nombre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='fechaCreacion',
        ),
        migrations.RemoveField(
            model_name='carrito',
            name='fechaModificacion',
        ),
        migrations.RemoveField(
            model_name='itemcarrito',
            name='carrito',
        ),
        migrations.RemoveField(
            model_name='itemcarrito',
            name='fechaCreacion',
        ),
        migrations.RemoveField(
            model_name='itemcarrito',
            name='fechaModificacion',
        ),
    ]
