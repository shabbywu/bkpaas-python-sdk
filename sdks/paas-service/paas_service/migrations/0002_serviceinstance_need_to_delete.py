# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-25 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paas_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceinstance',
            name='to_be_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
