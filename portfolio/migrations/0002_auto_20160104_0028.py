# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 00:28
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='slug', editable=False, populate_from='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='front_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='portfolioimage',
            name='file_path',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio'),
        ),
    ]