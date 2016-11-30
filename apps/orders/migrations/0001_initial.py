# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('city', models.CharField(max_length=60, default='Mexicali')),
                ('state', models.CharField(max_length=60, default='Baja California')),
                ('street', models.CharField(max_length=60)),
                ('number', models.IntegerField()),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=60, unique=True)),
                ('phone', models.CharField(max_length=60, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('address', models.OneToOneField(to='orders.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(to='orders.Customer')),
                ('employee', models.ForeignKey(to='accounts.EmployeeUser', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('measure', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=40)),
                ('serie', models.CharField(max_length=30)),
                ('design', models.CharField(max_length=30)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(to='orders.Order', related_name='items')),
            ],
        ),
    ]
