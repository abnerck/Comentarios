# Generated by Django 4.2.5 on 2023-09-15 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_nacimiento',
        ),
    ]
