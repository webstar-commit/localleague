# Generated by Django 2.2 on 2019-04-04 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('starts_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('sponser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Standings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games_played', models.IntegerField(default=0, verbose_name='Games Played')),
                ('points', models.IntegerField(default=0, verbose_name='Points')),
                ('wins', models.IntegerField(default=0, verbose_name='Wins')),
                ('draws', models.IntegerField(default=0, verbose_name='Draws')),
                ('losses', models.IntegerField(default=0, verbose_name='Losses')),
                ('league', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leagues.League')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('away_score', models.PositiveSmallIntegerField(blank=True)),
                ('home_score', models.PositiveSmallIntegerField(blank=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('result', models.CharField(choices=[('1', 'Away Team Wins!'), ('2', 'Home Team Wins!'), ('3', 'Draw!'), ('4', 'Pending')], default='4', max_length=1)),
                ('away', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='teams.Team')),
                ('home', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='teams.Team')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='leagues.Round')),
            ],
            options={
                'unique_together': {('away', 'home')},
            },
        ),
    ]