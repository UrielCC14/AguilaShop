# Generated by Django 4.2.5 on 2023-10-28 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_user_e_mail_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='zona',
            name='image',
            field=models.ImageField(null=True, upload_to='zones'),
        ),
    ]