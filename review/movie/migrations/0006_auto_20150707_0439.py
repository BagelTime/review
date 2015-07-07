# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20150705_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryrafting',
            name='category',
        ),
        migrations.RemoveField(
            model_name='categoryrafting',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='CategoryRafting',
        ),
    ]
