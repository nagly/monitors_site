# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitors', '0001_initial'),
        ('hyips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hyips_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('listing_id', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=1)),
                ('hyip_id', models.ForeignKey(to='hyips.Hyip')),
                ('monitor_id', models.ForeignKey(to='monitors.Monitor')),
            ],
        ),
    ]
