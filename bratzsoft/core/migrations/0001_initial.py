# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('hostname', models.CharField(max_length=100)),
                ('ipv4', models.GenericIPAddressField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LinkURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('description', models.TextField(max_length=500)),
                ('link', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('number', models.CharField(max_length=15)),
                ('version', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=200)),
                ('component', models.CharField(max_length=30)),
                ('update_date', models.DateTimeField()),
                ('related_product', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('sid', models.CharField(max_length=3)),
                ('instance_number', models.CharField(max_length=2)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Customer')),
                ('hosts', models.ManyToManyField(to='core.Host')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
