# Generated by Django 5.1.4 on 2025-04-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_habit_reset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='reset',
            field=models.BooleanField(default=True),
        ),
    ]
