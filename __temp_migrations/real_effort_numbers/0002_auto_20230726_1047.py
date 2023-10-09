# Generated by Django 2.2.12 on 2023-07-26 08:47

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('real_effort_numbers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='p10_cnt_mistakes',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p10_mistakes',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p10_time',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p1_cnt_mistakes',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p1_mistakes',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p1_time',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p2_cnt_mistakes',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p2_mistakes',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p2_time',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p3_cnt_mistakes',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p3_mistakes',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p3_time',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p4_cnt_mistakes',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p4_mistakes',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p4_time',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p5_cnt_mistakes',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p5_mistakes',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p5_time',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p6_cnt_mistakes',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p6_mistakes',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p6_time',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p7_cnt_mistakes',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p7_mistakes',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p7_time',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p8_cnt_mistakes',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p8_mistakes',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p8_time',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p9_cnt_mistakes',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p9_mistakes',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='p9_time',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]