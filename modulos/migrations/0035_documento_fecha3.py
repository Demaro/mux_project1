# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-01 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0034_documento_fecha2'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='fecha3',
            field=models.DateField(blank=True, null=True),
        ),
    ]
