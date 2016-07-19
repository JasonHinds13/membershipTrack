# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phillipo', '0005_auto_20160718_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='photo',
        ),
    ]
