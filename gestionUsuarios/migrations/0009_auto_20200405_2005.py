# Generated by Django 2.2.11 on 2020-04-05 18:05

import django.contrib.auth.models
from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuarios', '0008_auto_20200329_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioinfo',
            name='usuario',
            field=djongo.models.fields.EmbeddedField(model_container=django.contrib.auth.models.User, null=True),
        ),
    ]