# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 05:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='\u533f\u540d\u7528\u6237', max_length=20)),
                ('message', models.TextField()),
                ('del_pass', models.CharField(max_length=10)),
                ('pub_time', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=False)),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Mood')),
            ],
        ),
    ]
