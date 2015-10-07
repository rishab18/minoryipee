# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Code', models.IntegerField(null=True)),
                ('Title', models.CharField(max_length=26, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Final_price', models.IntegerField()),
                ('Sold_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InterestedIn',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Title', models.CharField(max_length=96)),
                ('BidStart', models.IntegerField()),
                ('BidPrice', models.IntegerField(blank=True, null=True)),
                ('Photos', models.ImageField(help_text='Upload image of your Product', upload_to='products_uploaded/', blank=True)),
                ('Timer', models.IntegerField()),
                ('On', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(max_length=1000, null=True)),
                ('By', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('Category', models.ManyToManyField(to='products.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='interestedin',
            name='Items',
            field=models.ManyToManyField(to='products.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='interestedin',
            name='User_interested',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='history',
            name='Item',
            field=models.ForeignKey(to='products.Product'),
            preserve_default=True,
        ),
    ]
