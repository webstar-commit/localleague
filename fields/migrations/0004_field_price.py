# Generated by Django 2.2 on 2019-04-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0003_field_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='price',
            field=models.FloatField(default=49.5),
            preserve_default=False,
        ),
    ]