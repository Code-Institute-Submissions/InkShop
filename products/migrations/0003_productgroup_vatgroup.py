# Generated by Django 3.0.7 on 2020-09-06 15:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200903_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profit_margin', models.IntegerField(default=30, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='VatGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('vat_rate', models.IntegerField(default=21, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
