# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-02 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0036_documento_firmasobr'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='suma_firmas',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
