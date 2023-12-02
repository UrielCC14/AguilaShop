# Generated by Django 4.2.5 on 2023-11-12 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0016_alter_tickets_comprado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale_Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(max_length=200, null=True)),
                ('total', models.CharField(max_length=200)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.targets')),
                ('ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.tickets')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]