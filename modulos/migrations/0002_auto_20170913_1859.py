# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-13 23:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carpetas',
            new_name='Carpeta',
        ),
        migrations.RenameField(
            model_name='submodulo',
            old_name='carpetas',
            new_name='carpeta',
        ),
    ]
