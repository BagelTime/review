# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=10, choices=[(b'G', b'G'), (b'PG', b'PG'), (b'PG-13', b'PG-13'), (b'R', b'R'), (b'NC-17', b'NC-17')])),
            ],
        ),
    ]
