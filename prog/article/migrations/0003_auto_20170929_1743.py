# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170812_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(verbose_name='Текст комментария'),
        ),
    ]
