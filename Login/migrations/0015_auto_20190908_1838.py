# Generated by Django 2.2.3 on 2019-09-08 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0014_auto_20190908_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='telefonoNumero',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]