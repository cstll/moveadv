# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdventureUser',
            fields=[
                ('user_id_num', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=255, null=True, blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, blank=True)),
                ('street_address', models.CharField(max_length=255, null=True, blank=True)),
                ('city', models.CharField(max_length=255, null=True, blank=True)),
                ('state', models.CharField(max_length=255, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=255, null=True, blank=True)),
                ('phone', models.CharField(max_length=255, null=True, blank=True)),
                ('gender', models.CharField(max_length=255, null=True, blank=True)),
                ('bday_month', models.IntegerField(default=1)),
                ('bday_day', models.IntegerField(default=1)),
                ('bday_year', models.IntegerField(default=0)),
                ('allergies', models.CharField(max_length=2000, null=True, blank=True)),
                ('found_us', models.CharField(max_length=2000, null=True, blank=True)),
                ('django_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('trip_id_num', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserTrips',
            fields=[
                ('user_trip_id_num', models.AutoField(serialize=False, primary_key=True)),
                ('trip', models.ForeignKey(to='adventures.Trip')),
                ('user', models.ForeignKey(to='adventures.AdventureUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
