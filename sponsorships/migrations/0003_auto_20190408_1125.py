# Generated by Django 2.2 on 2019-04-08 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsorships', '0002_delete_sponsor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsorshippackge',
            old_name='Type',
            new_name='type',
        ),
    ]
