# Generated by Django 2.2.3 on 2019-09-04 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_auto_20190811_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='telefonoNumero',
            field=models.IntegerField(default=0),
        ),
    ]
