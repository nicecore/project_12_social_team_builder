# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-11 15:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_application'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='application',
            name='position',
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]
