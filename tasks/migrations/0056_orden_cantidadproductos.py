# Generated by Django 4.2.5 on 2023-10-11 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0055_orden_idproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='cantidadProductos',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
