# Generated by Django 4.2.4 on 2023-10-09 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0031_alter_cliente_fecharegistro'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='fechaorden',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]