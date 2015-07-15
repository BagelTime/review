# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0017_auto_20150715_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_path',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(default=b'NR', max_length=10, choices=[(b'NR', b'NR'), (b'G', b'G'), (b'PG', b'PG'), (b'PG-13', b'PG-13'), (b'R', b'R'), (b'NC-17', b'NC-17')]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
