# Generated by Django 4.0.1 on 2022-06-18 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_alter_detallepedido_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallepedido',
            name='fechaModificacion',
        ),
        migrations.RemoveField(
            model_name='itemspedido',
            name='fechaModificacion',
        ),
        migrations.AddField(
            model_name='itemspedido',
            name='cantidad',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='itemspedido',
            name='detallePedido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.detallepedido'),
        ),
        migrations.AlterField(
            model_name='itemspedido',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.productopublico'),
        ),
    ]
