# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phillipo', '0010_auto_20160814_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='photo',
        ),
    ]
