# Generated by Django 4.2.2 on 2023-06-16 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_rename_games_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.game'),
        ),
    ]
