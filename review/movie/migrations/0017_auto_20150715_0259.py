# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0016_auto_20150715_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='summary',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
