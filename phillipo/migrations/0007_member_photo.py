# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('phillipo', '0006_remove_member_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='photo',
            field=models.ImageField(default=datetime.datetime(2016, 7, 18, 14, 44, 19, 223494, tzinfo=utc), upload_to=b'members_pics/'),
            preserve_default=False,
        ),
    ]
