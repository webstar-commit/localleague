# Generated by Django 2.2 on 2019-04-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0002_auto_20190404_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
