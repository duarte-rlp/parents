# Generated by Django 2.2.12 on 2023-09-13 11:06

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0002_auto_20230913_0536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='time_cultivos',
        ),
        migrations.AddField(
            model_name='player',
            name='time_cultivos_1',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='time_cultivos_2',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='time_cultivos_3',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='time_cultivos_4',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
