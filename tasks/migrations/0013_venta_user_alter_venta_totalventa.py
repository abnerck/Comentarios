# Generated by Django 4.2.5 on 2023-10-03 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0012_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='venta',
            name='totalVenta',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]