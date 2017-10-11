# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 03:26
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField()),
                ('color_code', colorful.fields.RGBColorField()),
                ('single_data', models.CharField(max_length=255, verbose_name='Single Data')),
                ('multipe_data', models.BooleanField(default=False, verbose_name='Multipe Data')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Graph',
                'verbose_name_plural': 'Graph',
            },
        ),
        migrations.CreateModel(
            name='GraphData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=250)),
                ('data', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('graph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='graph_data', to='graph.Graph')),
            ],
            options={
                'verbose_name': 'Graph Data',
                'verbose_name_plural': 'Graph Data',
            },
        ),
    ]