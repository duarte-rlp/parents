# Generated by Django 2.2.12 on 2023-09-23 23:54

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0028_auto_20230923_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='q_cropTypes',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
