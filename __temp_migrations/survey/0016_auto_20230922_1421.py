# Generated by Django 2.2.12 on 2023-09-22 19:21

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0015_auto_20230922_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='risk_list',
        ),
        migrations.AddField(
            model_name='player',
            name='q_risk_list',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
