# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guests", "0007_auto_20160207_2119"),
    ]

    operations = [
        migrations.AddField(
            model_name="party",
            name="invitation_id",
            field=models.CharField(blank=True, db_index=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="party",
            name="invitation_opened",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="party",
            name="invitation_sent",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
