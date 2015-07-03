# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20150625_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.FileField(upload_to=b'icons'),
        ),
    ]
