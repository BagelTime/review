# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='acting',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='action',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='adventure',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='alcohol_drug',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='bad_language',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='confusing',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='funny',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='gore',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='intelectual',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='kid_friendly',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='overall',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='romance',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='sad',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='scare',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='sexual',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='violence',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
    ]
