# Generated by Django 4.2.5 on 2023-11-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_shipping_address_user_targets_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='order_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
