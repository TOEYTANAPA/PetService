# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-04 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0019_auto_20170504_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='dogOwner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authapp.Person'),
        ),
    ]