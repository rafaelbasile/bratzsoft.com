# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 01:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='account',
            new_name='user',
        ),
    ]