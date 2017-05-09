# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-07 05:47
from __future__ import unicode_literals

import angelapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('cslug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmotionRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('emotion', models.CharField(max_length=100)),
                ('emotion_image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=angelapp.models.upload_location_image, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pslug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=angelapp.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('pkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='angelapp.Company')),
            ],
        ),
        migrations.CreateModel(
            name='TextRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('pkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='angelapp.Product')),
            ],
        ),
        migrations.AddField(
            model_name='emotionrating',
            name='pkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='angelapp.Product'),
        ),
    ]