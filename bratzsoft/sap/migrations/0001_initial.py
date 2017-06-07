# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 02:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
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
            name='LandscapeRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
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
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sap.Category')),
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
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sap.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=30)),
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
                ('hosts', models.ManyToManyField(to='sap.Host')),
                ('landscape_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sap.LandscapeRole')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
