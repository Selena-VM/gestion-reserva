# Generated by Django 4.2.7 on 2023-12-06 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500, verbose_name='Nombre')),
                ('direccion', models.TextField(max_length=1000, verbose_name='Direccion')),
                ('pais', models.CharField(max_length=50, verbose_name='Pais')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'ordering': ['-nombre'],
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo de Habitacion')),
                ('numero_maximo_personas', models.IntegerField(verbose_name='Numero maximo de personas')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('imagen', models.ImageField(upload_to='', verbose_name='Imagen')),
                ('persona', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservas.persona', verbose_name='Persona')),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
                'ordering': ['-numero_maximo_personas'],
            },
        ),
    ]