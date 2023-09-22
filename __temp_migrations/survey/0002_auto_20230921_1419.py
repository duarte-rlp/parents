# Generated by Django 2.2.12 on 2023-09-21 19:19

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='p_age',
        ),
        migrations.RemoveField(
            model_name='player',
            name='p_sex',
        ),
        migrations.AddField(
            model_name='player',
            name='q_married',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
