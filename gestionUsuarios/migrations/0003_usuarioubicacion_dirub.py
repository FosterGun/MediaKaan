# Generated by Django 2.2.13 on 2020-06-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuarios', '0002_auto_20200628_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarioubicacion',
            name='dirUb',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
