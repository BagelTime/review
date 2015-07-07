# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_auto_20150707_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='id',
        ),
        migrations.AlterField(
            model_name='movie',
            name='db_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
