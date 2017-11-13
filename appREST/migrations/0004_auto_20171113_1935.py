# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 21:35
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appREST', '0003_auto_20171113_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(Decimal('50.00'))]),
        ),
    ]
