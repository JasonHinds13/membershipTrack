# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('phillipo', '0011_remove_member_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='photo',
            field=models.ImageField(default=datetime.datetime(2016, 8, 14, 16, 2, 36, 645164, tzinfo=utc), upload_to=b'images/'),
            preserve_default=False,
        ),
    ]
