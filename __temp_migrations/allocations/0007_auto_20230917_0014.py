# Generated by Django 2.2.12 on 2023-09-17 05:14

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0006_auto_20230916_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='val_invesment_1',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='val_invesment_2',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
