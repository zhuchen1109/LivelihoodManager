# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-16 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ll_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='bankNum',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='fatherPhone',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='friendPhone',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='motherPhone',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='phone',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='unitPhone',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='wifePhone',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='workmatePhone',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
