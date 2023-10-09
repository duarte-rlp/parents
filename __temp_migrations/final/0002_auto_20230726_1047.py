# Generated by Django 2.2.12 on 2023-07-26 08:47

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='pago_total',
        ),
        migrations.AddField(
            model_name='player',
            name='activity_pay',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='pago_real',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
