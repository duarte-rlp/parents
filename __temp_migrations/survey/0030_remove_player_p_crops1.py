# Generated by Django 2.2.12 on 2023-09-23 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0029_player_q_croptypes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='p_crops1',
        ),
    ]
