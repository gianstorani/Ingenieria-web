# Generated by Django 2.2.3 on 2019-09-05 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0006_auto_20190905_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='fechaNacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
