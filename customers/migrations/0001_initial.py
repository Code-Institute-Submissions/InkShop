# Generated by Django 3.0.7 on 2020-09-13 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_phone_number', models.CharField(blank=True, max_length=254, null=True)),
                ('billing_address_line1', models.CharField(blank=True, max_length=254, null=True)),
                ('billing_address_line2', models.CharField(blank=True, max_length=254, null=True)),
                ('billing_town_or_city', models.CharField(blank=True, max_length=254, null=True)),
                ('billing_county', models.CharField(blank=True, max_length=254, null=True)),
                ('billing_post_code', models.CharField(blank=True, max_length=254, null=True)),
                ('billing_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_ref', models.CharField(max_length=60)),
                ('contact_name', models.CharField(blank=True, max_length=254, null=True)),
                ('contact_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address_line1', models.CharField(blank=True, max_length=254, null=True)),
                ('address_line2', models.CharField(blank=True, max_length=254, null=True)),
                ('town_or_city', models.CharField(blank=True, max_length=254, null=True)),
                ('county', models.CharField(blank=True, max_length=254, null=True)),
                ('post_code', models.CharField(blank=True, max_length=254, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_address', to='customers.UserProfile')),
            ],
        ),
    ]
