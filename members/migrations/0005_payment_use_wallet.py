# Generated by Django 4.1.5 on 2023-01-30 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_member_phonenumber_alter_payment_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='use_wallet',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
