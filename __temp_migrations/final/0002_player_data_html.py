# Generated by Django 2.2.12 on 2023-09-24 17:46

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='data_html',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]