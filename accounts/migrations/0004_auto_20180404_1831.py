# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180404_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(choices=[('android', 'Android Developer'), ('designer', 'Designer'), ('java', 'Java Developer'), ('php', 'PHP Developer'), ('python', 'Python Developer'), ('rails', 'Rails Developer'), ('wordpress', 'Wordpress Devloper'), ('ios', 'iOS Developer')], default='', max_length=8),
        ),
    ]
