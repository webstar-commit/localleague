# Generated by Django 2.2 on 2019-04-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0002_auto_20190407_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='away_score',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_score',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
