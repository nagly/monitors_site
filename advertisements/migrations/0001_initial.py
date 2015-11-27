# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(max_length=1)),
                ('image', models.ImageField(upload_to=b'banners')),
                ('url', models.CharField(max_length=100)),
                ('weeks', models.PositiveIntegerField(default=1)),
                ('price', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expiration', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Buffer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(max_length=1)),
                ('image', models.ImageField(upload_to=b'banners')),
                ('url', models.CharField(max_length=100)),
                ('weeks', models.PositiveIntegerField(default=1)),
                ('price', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expiration', models.DateTimeField(null=True, blank=True)),
                ('unique_id', models.CharField(default=uuid.uuid4, unique=True, max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OldOne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(max_length=1)),
                ('image', models.ImageField(upload_to=b'banners')),
                ('url', models.CharField(max_length=100)),
                ('weeks', models.PositiveIntegerField(default=1)),
                ('price', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
