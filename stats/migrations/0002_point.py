# Generated by Django 4.0.2 on 2022-02-09 02:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
        ('players', '0001_initial'),
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('identifier', models.CharField(choices=[('minutes', 'minutes'), ('goals_scored', 'goals_scored'), ('assists', 'assists'), ('clean_sheets', 'clean_sheets'), ('goals_conceded', 'goals_conceded'), ('own_goals', 'own_goals'), ('penalties_saved', 'penalties_saved'), ('penalties_missed', 'penalties_missed'), ('yellow_cards', 'yellow_cards'), ('red_cards', 'red_cards'), ('saves', 'saves'), ('bonus', 'bonus')], max_length=32)),
                ('number', models.IntegerField(default=0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='matches.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='players.player')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]