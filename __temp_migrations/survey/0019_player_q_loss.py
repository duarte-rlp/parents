# Generated by Django 2.2.12 on 2023-09-23 23:06

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0018_auto_20230923_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='q_loss',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
