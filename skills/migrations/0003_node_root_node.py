# Generated by Django 5.1.4 on 2025-05-10 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_tree_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='root_node',
            field=models.BooleanField(default=False),
        ),
    ]
