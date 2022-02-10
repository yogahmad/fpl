# Generated by Django 4.0.2 on 2022-02-10 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0003_alter_player_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="chance_of_playing_next_round",
            field=models.IntegerField(
                blank=True,
                choices=[(100, 0), (75, 75), (50, 50), (25, 25)],
                default=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="chance_of_playing_this_round",
            field=models.IntegerField(
                blank=True,
                choices=[(100, 0), (75, 75), (50, 50), (25, 25)],
                default=100,
                null=True,
            ),
        ),
    ]
