# Generated by Django 3.1.7 on 2021-03-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0002_enterprise_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='nit',
            field=models.CharField(max_length=50, unique=True, verbose_name='NIT'),
        ),
    ]
