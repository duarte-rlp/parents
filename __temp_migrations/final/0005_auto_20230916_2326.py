# Generated by Django 2.2.12 on 2023-09-17 04:26

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0004_player_pago_base'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='is_menor_pago',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
    ]
