# Generated by Django 2.2.6 on 2019-10-07 14:41

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
