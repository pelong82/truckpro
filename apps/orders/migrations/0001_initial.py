# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('measure', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=40)),
                ('serie', models.CharField(max_length=30)),
                ('design', models.CharField(max_length=30)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TimeStampModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, auto_created=True, to='orders.TimeStampModel')),
                ('name', models.CharField(unique=True, max_length=80)),
                ('rfc', models.CharField(unique=True, max_length=15)),
                ('city', models.CharField(default='Mexicali', max_length=60)),
                ('colony', models.CharField(max_length=60)),
                ('state', models.CharField(default='Baja California', max_length=60)),
                ('street', models.CharField(max_length=60)),
                ('number', models.IntegerField()),
                ('zip_code', models.IntegerField()),
                ('phone', models.CharField(unique=True, max_length=60)),
            ],
            bases=('orders.timestampmodel',),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, auto_created=True, to='orders.TimeStampModel')),
                ('is_active', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(to='orders.Customer')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('orders.timestampmodel',),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(to='orders.Order'),
        ),
    ]
