# Generated by Django 5.1.4 on 2025-05-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_habit_streak'),
        ('skills', '0010_node_difficulty_node_time_required_tree_exp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='skills',
            field=models.ManyToManyField(null=True, to='skills.tree'),
        ),
    ]
