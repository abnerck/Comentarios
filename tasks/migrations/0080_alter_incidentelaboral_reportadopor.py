# Generated by Django 4.2.5 on 2023-10-31 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0079_alter_ticket_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentelaboral',
            name='reportadopor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
