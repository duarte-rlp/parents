# Generated by Django 2.2.12 on 2023-09-12 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0003_auto_20230912_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='problem_02_var',
        ),
        migrations.RemoveField(
            model_name='player',
            name='problem_03_var',
        ),
        migrations.RemoveField(
            model_name='player',
            name='problem_04_var',
        ),
    ]