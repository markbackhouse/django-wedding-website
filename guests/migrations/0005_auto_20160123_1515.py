# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-23 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guests", "0004_party_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="party",
            name="type",
            field=models.CharField(
                choices=[("formal", "formal"), ("fun", "fun"), ("dimagi", "dimagi")],
                max_length=10,
            ),
        ),
    ]
