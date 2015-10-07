# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20151001_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(null=True, unique=True, help_text='Only Indian', max_length=13),
        ),
    ]
