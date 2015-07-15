# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0015_review_reviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.CharField(default=b'?', max_length=100),
        ),
    ]
