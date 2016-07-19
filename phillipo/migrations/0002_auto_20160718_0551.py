# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('phillipo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='birth_day',
            field=models.CharField(default=datetime.datetime(2016, 7, 18, 5, 51, 10, 556429, tzinfo=utc), max_length=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='birth_month',
            field=models.CharField(default=datetime.datetime(2016, 7, 18, 5, 51, 17, 736203, tzinfo=utc), max_length=1, choices=[(b'Jan', b'January'), (b'Feb', b'February'), (b'Mar', b'March'), (b'Apr', b'April'), (b'May', b'May'), (b'Jun', b'June'), (b'Jul', b'July'), (b'Aug', b'August'), (b'Sep', b'September'), (b'Oct', b'October'), (b'Nov', b'November'), (b'Dec', b'December')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='birth_year',
            field=models.CharField(default=datetime.datetime(2016, 7, 18, 5, 51, 24, 701881, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(upload_to=b'members_pics/'),
        ),
    ]
