# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0019_auto_20150715_0425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='acting',
        ),
        migrations.RemoveField(
            model_name='review',
            name='confusing',
        ),
    ]
