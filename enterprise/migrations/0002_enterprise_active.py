# Generated by Django 3.1.7 on 2021-03-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprise',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
