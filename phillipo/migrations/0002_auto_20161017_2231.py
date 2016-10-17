# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('phillipo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cell_phonenumber',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='church',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email_address',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='home_address',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='home_phonenumber',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='relationship',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='work_address',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='work_phonenumber',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='additional_remarks',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='baptised_by',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='birth_day',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30'), (b'31', b'31')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='birth_month',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Jan', b'January'), (b'Feb', b'February'), (b'Mar', b'March'), (b'Apr', b'April'), (b'May', b'May'), (b'Jun', b'June'), (b'Jul', b'July'), (b'Aug', b'August'), (b'Sep', b'September'), (b'Oct', b'October'), (b'Nov', b'November'), (b'Dec', b'December')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='birth_year',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='cell_phonenumber',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='church_activity',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='church_of_baptism',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='classNumber',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='clubs',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='contact',
            field=models.OneToOneField(null=True, blank=True, to='phillipo.Contact'),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_baptism',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_conversion',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_phillippo_membership',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='email_address',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='highest_level_of_education',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Primary', b'Primary'), (b'Secondary', b'Secondary'), (b'Tertiary', b'Tertiary')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='hobbies',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='home_address',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='home_phonenumber',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Single', b'Single'), (b'Married', b'Married'), (b'Divorced', b'Divorced'), (b'Widowed', b'Widowed')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='number_of_children',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name=b'pro_pic', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='place_of_birth',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='previous_church',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='profession',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='qualification',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='skills',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='website',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='work_address',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='work_phonenumber',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
