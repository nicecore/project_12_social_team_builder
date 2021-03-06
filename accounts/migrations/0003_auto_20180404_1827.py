# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.ManyToManyField(to='accounts.Skill'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(choices=[('1', 'Android Developer'), ('2', 'Designer'), ('3', 'Java Developer'), ('4', 'PHP Developer'), ('5', 'Python Developer'), ('6', 'Rails Developer'), ('7', 'Wordpress Devloper'), ('8', 'iOS Developer')], default='', max_length=8),
        ),
    ]
