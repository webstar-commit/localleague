# Generated by Django 2.2 on 2019-04-08 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_sponsor_packge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='packge',
            new_name='package',
        ),
    ]
