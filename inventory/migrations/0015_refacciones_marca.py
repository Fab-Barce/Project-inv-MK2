# Generated by Django 5.2 on 2025-04-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_vehiculo_num_unidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='refacciones',
            name='marca',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
