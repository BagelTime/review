# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_auto_20150707_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(null=True, blank=True),
        ),
    ]
