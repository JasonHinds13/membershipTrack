# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name=b'pro_pic')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('birth_month', models.CharField(max_length=255, choices=[(b'Jan', b'January'), (b'Feb', b'February'), (b'Mar', b'March'), (b'Apr', b'April'), (b'May', b'May'), (b'Jun', b'June'), (b'Jul', b'July'), (b'Aug', b'August'), (b'Sep', b'September'), (b'Oct', b'October'), (b'Nov', b'November'), (b'Dec', b'December')])),
                ('birth_day', models.CharField(max_length=255, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30'), (b'31', b'31')])),
                ('birth_year', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=255)),
                ('ministry', models.CharField(max_length=255)),
                ('classNumber', models.CharField(max_length=255)),
            ],
        ),
    ]
