# Generated by Django 2.2 on 2019-04-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0006_participateinvite_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='fees_per_team',
            field=models.FloatField(default=99.0),
        ),
    ]
