# Generated by Django 3.1.7 on 2021-03-25 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre empresa')),
                ('address', models.CharField(max_length=50, verbose_name='Direccion')),
                ('nit', models.CharField(max_length=50, verbose_name='NIT')),
                ('phone', models.CharField(max_length=10, verbose_name='Telefono')),
            ],
        ),
    ]
