# Generated by Django 4.1.5 on 2023-02-06 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_alter_payment_payment_release'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_release',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 6, 20, 18, 35, 920843, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
