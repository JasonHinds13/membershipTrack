# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phillipo', '0018_member_birth_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birth_month',
            field=models.CharField(max_length=255, choices=[(b'Jan', b'January'), (b'Feb', b'February'), (b'Mar', b'March'), (b'Apr', b'April'), (b'May', b'May'), (b'Jun', b'June'), (b'Jul', b'July'), (b'Aug', b'August'), (b'Sep', b'September'), (b'Oct', b'October'), (b'Nov', b'November'), (b'Dec', b'December')]),
        ),
    ]
