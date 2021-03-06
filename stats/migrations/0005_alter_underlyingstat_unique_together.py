# Generated by Django 4.0.2 on 2022-02-14 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0002_player_understat_id"),
        ("matches", "0001_initial"),
        ("stats", "0004_underlyingstat_player"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="underlyingstat",
            unique_together={("match", "player")},
        ),
    ]
