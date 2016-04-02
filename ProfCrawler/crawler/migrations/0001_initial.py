# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('url', models.CharField(default=b'', max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('current_position', models.TextField()),
                ('summary', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('count_top_skills', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(to='crawler.Skill'),
        ),
    ]
