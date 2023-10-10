# Generated by Django 3.2.8 on 2023-10-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('TipoSolicitud', models.CharField(max_length=100, verbose_name='Tipo de solicitud')),
                ('Descripcion', models.TextField(verbose_name='Descripcion')),
                ('Imagen', models.ImageField(upload_to='images/actividades/', verbose_name='Imagen')),
                ('fecha_actividad', models.DateField(verbose_name='Fecha de actividad')),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('Descripcion', models.TextField(verbose_name='Descripcion')),
                ('Imagen', models.ImageField(upload_to='images/noticias/', verbose_name='Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Propuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('TipoSolicitud', models.CharField(max_length=100, verbose_name='Tipo de solicitud')),
                ('Descripcion', models.TextField(verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('TipoProyecto', models.CharField(max_length=100, verbose_name='Tipo de proyecto')),
                ('Descripcion', models.TextField(verbose_name='Descripcion')),
                ('Imagen', models.ImageField(upload_to='images/proyectos/', verbose_name='Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Vecinos',
            fields=[
                ('rut', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('correo', models.EmailField(max_length=100, verbose_name='Correo')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('certificado', models.ImageField(upload_to='images/', verbose_name='Certificado de residencia')),
            ],
        ),
    ]
