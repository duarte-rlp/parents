# Generated by Django 2.2.12 on 2023-09-24 16:45

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0034_player_q_savings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='p_savings',
            field=otree.db.models.IntegerField(choices=[[1, 'Sí'], [2, 'No'], [3, 'No cultivo ningún cultivo / No lo sé']], null=True, verbose_name=''),
        ),
    ]
