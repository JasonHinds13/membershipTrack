# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phillipo', '0009_auto_20160812_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='birth_day',
            field=models.TextField(max_length=31, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30'), (b'31', b'31')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='birth_month',
            field=models.TextField(max_length=9, choices=[(b'Jan', b'January'), (b'Feb', b'February'), (b'Mar', b'March'), (b'Apr', b'April'), (b'May', b'May'), (b'Jun', b'June'), (b'Jul', b'July'), (b'Aug', b'August'), (b'Sep', b'September'), (b'Oct', b'October'), (b'Nov', b'November'), (b'Dec', b'December')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='birth_year',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='classNumber',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='ministry',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='profession',
            field=models.TextField(max_length=255),
        ),
    ]
