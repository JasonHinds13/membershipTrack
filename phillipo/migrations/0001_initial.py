# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'members/')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=255)),
                ('ministry', models.CharField(max_length=255)),
                ('classNumber', models.CharField(max_length=255)),
            ],
        ),
    ]
