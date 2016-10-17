# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phillipo', '0002_auto_20161017_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='cell_phonenumber',
            new_name='contact_cell_phonenumber',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='church',
            new_name='contact_church',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='email_address',
            new_name='contact_email_address',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='home_address',
            new_name='contact_home_address',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='home_phonenumber',
            new_name='contact_home_phonenumber',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='contact_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='relationship',
            new_name='contact_relationship',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='work_address',
            new_name='contact_work_address',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='work_phonenumber',
            new_name='contact_work_phonenumber',
        ),
    ]
