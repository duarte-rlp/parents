# Generated by Django 2.2.12 on 2023-09-22 19:17

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0012_player_q_risk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='p_risk1',
            field=otree.db.models.IntegerField(null=True, verbose_name='¿Cuándo estás decidiendo sobre tus inversiones que tanto riesgo estás dispuesto a asumir?'),
        ),
    ]