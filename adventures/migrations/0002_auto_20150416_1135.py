# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventures', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertrips',
            options={'managed': True, 'verbose_name_plural': 'User Trips'},
        ),
    ]
