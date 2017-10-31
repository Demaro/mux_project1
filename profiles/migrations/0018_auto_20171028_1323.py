# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-28 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_auto_20171028_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil_obrero',
            name='especialidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Especialidad'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='especialidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Especialidad_staff'),
        ),
    ]