# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-16 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0010_article_domain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='domain',
        ),
        migrations.AddField(
            model_name='post',
            name='domain',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
