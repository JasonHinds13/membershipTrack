# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_name', models.CharField(max_length=255, null=True, blank=True)),
                ('contact_relationship', models.CharField(max_length=255, null=True, blank=True)),
                ('contact_home_address', models.CharField(max_length=255, null=True, blank=True)),
                ('contact_work_address', models.CharField(max_length=255, null=True, blank=True)),
                ('contact_email_address', models.CharField(max_length=255, null=True, blank=True)),
                ('contact_cell_phonenumber', models.CharField(max_length=255, null=True, blank=True)),
                ('contact_home_phonenumber', models.CharField(max_length=255, null=True, blank=True)),
                ('contact_work_phonenumber', models.CharField(max_length=255, null=True, blank=True)),
                ('contact_church', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name=b'pro_pic', blank=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('classNumber', models.CharField(max_length=255, null=True, blank=True)),
                ('memberNumber', models.CharField(max_length=255, null=True, blank=True)),
                ('employed', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('pensioner', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('membership_status', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Current', b'Current'), (b'Inactive', b'Inactive'), (b'Migrated', b'Migrated'), (b'Transfered', b'Transfered'), (b'Shut-in', b'Shut-in')])),
                ('home_phonenumber', models.CharField(max_length=255, null=True, blank=True)),
                ('cell_phonenumber', models.CharField(max_length=255, null=True, blank=True)),
                ('work_phonenumber', models.CharField(max_length=255, null=True, blank=True)),
                ('home_address', models.CharField(max_length=255, null=True, blank=True)),
                ('work_address', models.CharField(max_length=255, null=True, blank=True)),
                ('email_address', models.CharField(max_length=255, null=True, blank=True)),
                ('website', models.CharField(max_length=255, null=True, blank=True)),
                ('previous_church', models.CharField(max_length=255, null=True, blank=True)),
                ('birth_month', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Jan', b'January'), (b'Feb', b'February'), (b'Mar', b'March'), (b'Apr', b'April'), (b'May', b'May'), (b'Jun', b'June'), (b'Jul', b'July'), (b'Aug', b'August'), (b'Sep', b'September'), (b'Oct', b'October'), (b'Nov', b'November'), (b'Dec', b'December')])),
                ('birth_day', models.CharField(blank=True, max_length=255, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30'), (b'31', b'31')])),
                ('birth_year', models.CharField(max_length=255, null=True, blank=True)),
                ('place_of_birth', models.CharField(max_length=255, null=True, blank=True)),
                ('marital_status', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Single', b'Single'), (b'Married', b'Married'), (b'Divorced', b'Divorced'), (b'Widowed', b'Widowed')])),
                ('number_of_children', models.CharField(max_length=255, null=True, blank=True)),
                ('highest_level_of_education', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Primary', b'Primary'), (b'Secondary', b'Secondary'), (b'Tertiary', b'Tertiary')])),
                ('qualification', models.CharField(max_length=255, null=True, blank=True)),
                ('skills', models.CharField(max_length=255, null=True, blank=True)),
                ('hobbies', models.CharField(max_length=255, null=True, blank=True)),
                ('date_of_conversion', models.CharField(max_length=255, null=True, blank=True)),
                ('date_of_baptism', models.CharField(max_length=255, null=True, blank=True)),
                ('church_of_baptism', models.CharField(max_length=255, null=True, blank=True)),
                ('baptised_by', models.CharField(max_length=255, null=True, blank=True)),
                ('date_of_phillippo_membership', models.CharField(max_length=255, null=True, blank=True)),
                ('clubs', models.CharField(max_length=255, null=True, blank=True)),
                ('church_activity', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Brotherhood', b'Brotherhood'), (b'Womens Federation', b'Womens Federation'), (b'Ushers Board', b'Ushers Board'), (b'Youth Fellowship', b'Youth Fellowship'), (b'Young Adult', b'Young Adult')])),
                ('special_ministries', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Audio Visual', b'Audio Visual'), (b'Creative Arts', b'Creative Arts'), (b'Family Life', b'Family Life'), (b'Education/Continuing Education Programme', b'Education/Continuing Education Programme'), (b'Harvest', b'Harvest'), (b'Hospitatlity', b'Hospitatlity'), (b'Mission/Evangelism', b'Mission/Evangelism'), (b'Medicare, Counselling and Healing', b'Medicare, Counselling and Healing'), (b'Music', b'Music'), (b'Property and Building', b'Property and Building'), (b'Social Outreach', b'Social Outreach'), (b'Sports Ministry', b'Sports Ministry'), (b'Sunday School', b'Sunday School'), (b'Stewartship/Training', b'Stewartship/Training'), (b'Welfare/Benevolence', b'Welfare/Benevolence')])),
                ('profession', models.CharField(max_length=255, null=True, blank=True)),
                ('additional_remarks', models.CharField(max_length=255, null=True, blank=True)),
                ('contact', models.OneToOneField(null=True, blank=True, to='phillipo.Contact')),
            ],
        ),
    ]
