# Generated by Django 4.1.5 on 2023-01-22 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_payment_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phonenumber',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment',
            field=models.IntegerField(),
        ),
    ]
