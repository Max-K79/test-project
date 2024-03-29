# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 01:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_text', models.TextField()),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='article_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article'),
        ),
    ]
