# Generated by Django 2.2 on 2019-04-08 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_playerinvite_teamrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerinvite',
            name='expire_date',
        ),
        migrations.RemoveField(
            model_name='teamrequest',
            name='expire_date',
        ),
    ]
