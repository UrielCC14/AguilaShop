# Generated by Django 4.2.5 on 2023-10-14 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imagen',
            field=models.BinaryField(default=b''),
        ),
        migrations.AddField(
            model_name='product',
            name='temporada',
            field=models.CharField(default='temporada', max_length=200),
        ),
    ]