# Generated by Django 4.2.5 on 2024-01-03 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0106_alter_venta_fechaventa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipocliente',
            field=models.CharField(blank=True, choices=[('Mayorista', 'Mayorista'), ('Menudista', 'Menudista')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='totalCompra',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='herramienta',
            name='estadoHerramienta',
            field=models.CharField(blank=True, choices=[('Activo', 'Activo'), ('Desactivado', 'Desactivado')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='costo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='estadodelprovedor',
            field=models.TextField(blank=True, choices=[('Activo', 'Activo'), ('Desactivado', 'Desactivado')], null=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='totalVenta',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]