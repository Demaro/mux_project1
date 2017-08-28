# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-28 17:30
from __future__ import unicode_literals

import activitys.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=activitys.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('fecha_inicio', models.DateField(auto_now=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('fecha_termino', models.DateTimeField(auto_now=True, null=True)),
                ('user_asign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignado', to=settings.AUTH_USER_MODEL)),
                ('user_create', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_create', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
