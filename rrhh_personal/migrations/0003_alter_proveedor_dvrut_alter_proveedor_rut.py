# Generated by Django 5.1.3 on 2025-01-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh_personal', '0002_claselicencia_resultadoexamen_tipocertificacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='dvRut',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='rut',
            field=models.CharField(max_length=8),
        ),
    ]
