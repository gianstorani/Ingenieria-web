# Generated by Django 2.2.3 on 2019-09-03 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('idComentario', models.AutoField(primary_key=True, serialize=False)),
                ('contenidoComentario', models.TextField(null=True)),
                ('fechaComentario', models.DateField(auto_now=True, verbose_name='Date')),
                ('fechaModiComentario', models.DateField(default=None, editable=False, null=True)),
                ('fechaBajaComentario', models.DateField(default=None, editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('idPublicacion', models.AutoField(primary_key=True, serialize=False)),
                ('tituloPublicacion', models.CharField(max_length=50)),
                ('Contenido', models.TextField()),
                ('FechaPublicacion', models.DateField(auto_now=True, verbose_name='Date')),
                ('FechaBajaPublicacion', models.DateField(default=None, editable=False, null=True)),
                ('FechaModificacionPublicacion', models.DateField(default=None, editable=False, null=True)),
                ('idUsuarioPublicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAlta', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('fechaBaja', models.DateTimeField(blank=True, null=True)),
                ('motivoBaja', models.CharField(blank=True, max_length=200, null=True)),
                ('idComentario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sitio.Comentario')),
                ('idPublicacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sitio.Publicacion')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='idPublicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sitio.Publicacion'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='idUsuarioComentario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]