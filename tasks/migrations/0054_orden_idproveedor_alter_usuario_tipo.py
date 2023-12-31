# Generated by Django 4.2.5 on 2023-10-11 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0053_remove_cliente_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='idProveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.proveedor'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('Gerente', 'Gerente'), ('Empleado', 'Empleado')], max_length=100),
        ),
    ]
