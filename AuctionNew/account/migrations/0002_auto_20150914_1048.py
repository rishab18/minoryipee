# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='Phone',
        ),
        migrations.AddField(
            model_name='myuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Only Indian', null=True, max_length=128, unique=True),
            preserve_default=True,
        ),
    ]
