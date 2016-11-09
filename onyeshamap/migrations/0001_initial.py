# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus_Stops',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_id', models.IntegerField()),
                ('stop_id', models.CharField(max_length=254)),
                ('stop_name', models.CharField(max_length=254)),
                ('stop_lat', models.CharField(max_length=254)),
                ('stop_lon', models.CharField(max_length=254)),
                ('parent_sta', models.CharField(max_length=254)),
                ('route_1', models.CharField(max_length=254)),
                ('route_2', models.CharField(max_length=254)),
                ('route_3', models.CharField(max_length=254)),
                ('route_4', models.CharField(max_length=254)),
                ('route_5', models.CharField(max_length=254)),
                ('route_6', models.CharField(max_length=254)),
                ('route_7', models.CharField(max_length=254)),
                ('route_8', models.CharField(max_length=254)),
                ('route_9', models.CharField(max_length=254)),
                ('route_10', models.CharField(max_length=254)),
                ('route_11', models.CharField(max_length=254)),
                ('route_12', models.CharField(max_length=254)),
                ('route_13', models.CharField(max_length=254)),
                ('route_14', models.CharField(max_length=254)),
                ('route_15', models.CharField(max_length=254)),
                ('route_16', models.CharField(max_length=254)),
                ('route_17', models.CharField(max_length=254)),
                ('route_18', models.CharField(max_length=254)),
                ('route_19', models.CharField(max_length=254)),
                ('route_20', models.CharField(max_length=254)),
                ('route_21', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=32737)),
            ],
            options={
                'verbose_name': 'Bus Stops',
            },
        ),
        migrations.CreateModel(
            name='CCTV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('objectid', models.IntegerField()),
                ('type', models.CharField(max_length=254)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('eastings', models.FloatField()),
                ('northings', models.FloatField()),
                ('st_name', models.CharField(max_length=254)),
                ('descriptio', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=32737)),
            ],
            options={
                'verbose_name': 'CCTV Data',
            },
        ),
    ]
