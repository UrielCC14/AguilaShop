# Generated by Django 4.2.5 on 2023-10-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_tickets_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='e_mail',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
