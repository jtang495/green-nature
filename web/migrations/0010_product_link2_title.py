# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-11 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_product_name2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='link2_title',
            field=models.TextField(default=''),
        ),
    ]