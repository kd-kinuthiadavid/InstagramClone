# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_instagram', '0002_remove_likes_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes_for', to='my_instagram.Image'),
        ),
    ]
