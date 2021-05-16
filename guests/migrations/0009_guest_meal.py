# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-20 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guests", "0008_auto_20160214_1642"),
    ]

    operations = [
        migrations.AddField(
            model_name="guest",
            name="meal",
            field=models.CharField(
                blank=True,
                choices=[
                    ("beef", "Cow"),
                    ("chicken", "Chicken"),
                    ("vegetarian", "Vegetable"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
