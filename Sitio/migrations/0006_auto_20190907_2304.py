# Generated by Django 2.2.3 on 2019-09-07 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sitio', '0005_auto_20190907_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacion',
            old_name='localidad',
            new_name='localidadPublicacion',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='provincia',
            new_name='provinciaPublicacion',
        ),
    ]