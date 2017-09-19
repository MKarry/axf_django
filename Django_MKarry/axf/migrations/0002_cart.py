# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=10)),
                ('productid', models.CharField(max_length=10)),
                ('productnum', models.IntegerField()),
                ('productprice', models.FloatField()),
                ('productlongname', models.CharField(max_length=100)),
                ('productimg', models.CharField(max_length=150)),
                ('ischose', models.BooleanField()),
                ('isdelete', models.BooleanField()),
            ],
        ),
    ]
