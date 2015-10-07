# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('BidPrice', models.IntegerField()),
                ('By', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='BidStart',
            field=models.IntegerField(null=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='Category',
            field=models.ForeignKey(to='products.Category', null=True),
        ),
        migrations.AddField(
            model_name='bids',
            name='Item',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
