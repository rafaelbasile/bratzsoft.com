# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 00:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sap', '0002_auto_20170802_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='ipv4',
        ),
    ]
