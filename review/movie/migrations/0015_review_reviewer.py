# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0014_auto_20150711_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.CharField(default='?', max_length=100),
            preserve_default=False,
        ),
    ]
