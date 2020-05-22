# Generated by Django 3.0.3 on 2020-05-22 14:04

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('foodwagon_backend', '0002_venues_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venues',
            name='Phone',
            field=phone_field.models.PhoneField(blank=True, default=0, help_text='Contact phone number', max_length=31),
        ),
    ]
