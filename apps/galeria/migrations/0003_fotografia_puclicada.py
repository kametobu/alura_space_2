# Generated by Django 4.1.4 on 2023-05-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='puclicada',
            field=models.BooleanField(default=False),
        ),
    ]
