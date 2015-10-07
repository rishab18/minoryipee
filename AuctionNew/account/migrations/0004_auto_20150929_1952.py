# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_myuser_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='Address',
            field=models.ForeignKey(null=True, to='account.Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, unique=True, null=True, max_length=13, help_text='Only Indian'),
        ),
    ]
