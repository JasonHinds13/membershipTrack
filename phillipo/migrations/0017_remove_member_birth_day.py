# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phillipo', '0016_auto_20160814_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='birth_day',
        ),
    ]
