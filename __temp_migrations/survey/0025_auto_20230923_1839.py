# Generated by Django 2.2.12 on 2023-09-23 23:39

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0024_player_q_hectares'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='p_hectareas',
        ),
        migrations.AddField(
            model_name='player',
            name='q_farminc',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
