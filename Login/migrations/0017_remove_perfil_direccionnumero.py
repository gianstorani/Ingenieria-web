# Generated by Django 2.0.13 on 2019-09-15 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0016_auto_20190908_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='direccionNumero',
        ),
    ]
