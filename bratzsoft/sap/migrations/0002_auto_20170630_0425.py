# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sap', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abapuser',
            old_name='sid',
            new_name='sap_system',
        ),
        migrations.AlterField(
            model_name='note',
            name='number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='version',
            field=models.PositiveIntegerField(),
        ),
    ]
