# Generated by Django 4.0.2 on 2022-02-12 12:18

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("matches", "0001_initial"),
        ("teams", "0001_initial"),
        ("players", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UnderlyingStat",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("npxG", models.FloatField()),
                ("xA", models.FloatField()),
                ("shots", models.IntegerField()),
                ("key_passes", models.IntegerField()),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="matches.match"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Underlying stat",
            },
        ),
        migrations.CreateModel(
            name="TeamBettingOdd",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "identifier",
                    models.CharField(
                        choices=[("clean_sheets", "clean_sheets")], max_length=32
                    ),
                ),
                ("odd", models.FloatField(default=0.0)),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team_betting_odds",
                        to="matches.match",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team_betting_odds",
                        to="teams.team",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ShotsConcededData",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("expected_goal", models.FloatField()),
                (
                    "result",
                    models.CharField(
                        choices=[
                            ("Goal", "Goal"),
                            ("SavedShot", "Saved"),
                            ("BlockedShot", "Blocked"),
                            ("MissedShots", "Missed"),
                            ("ShotOnPost", "Shot On Post"),
                        ],
                        max_length=32,
                    ),
                ),
                ("minute", models.CharField(max_length=32)),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shots_data",
                        to="matches.match",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="teams.team"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Shots conceded data",
            },
        ),
        migrations.CreateModel(
            name="PreviousSeasonTotalPoint",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("season", models.CharField(max_length=32)),
                (
                    "identifier",
                    models.CharField(
                        choices=[
                            ("minutes", "minutes"),
                            ("goals_scored", "goals_scored"),
                            ("assists", "assists"),
                            ("clean_sheets", "clean_sheets"),
                            ("goals_conceded", "goals_conceded"),
                            ("own_goals", "own_goals"),
                            ("penalties_saved", "penalties_saved"),
                            ("penalties_missed", "penalties_missed"),
                            ("yellow_cards", "yellow_cards"),
                            ("red_cards", "red_cards"),
                            ("saves", "saves"),
                            ("bonus", "bonus"),
                        ],
                        max_length=32,
                    ),
                ),
                ("number", models.IntegerField(default=0)),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="previous_season_points",
                        to="matches.match",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="previous_season_points",
                        to="players.player",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PlayerBettingOdd",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "identifier",
                    models.CharField(
                        choices=[
                            ("goals_scored", "goals_scored"),
                            ("assists", "assists"),
                        ],
                        max_length=32,
                    ),
                ),
                ("odd", models.FloatField(default=0.0)),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="player_betting_odds",
                        to="matches.match",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="player_betting_odds",
                        to="players.player",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BonusPointSystem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("point", models.IntegerField(default=0)),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bpses",
                        to="matches.match",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bpses",
                        to="players.player",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Point",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "identifier",
                    models.CharField(
                        choices=[
                            ("minutes", "Minutes"),
                            ("goals_scored", "Goals scored"),
                            ("assists", "Assists"),
                            ("clean_sheets", "Clean sheets"),
                            ("goals_conceded", "Goals conceded"),
                            ("own_goals", "Own goals"),
                            ("penalties_saved", "Penalties saved"),
                            ("penalties_missed", "Penalties missed"),
                            ("yellow_cards", "Yellow cards"),
                            ("red_cards", "Red cards"),
                            ("saves", "Saves"),
                            ("bonus", "Bonus"),
                        ],
                        max_length=32,
                    ),
                ),
                ("number", models.IntegerField(default=0)),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="points",
                        to="matches.match",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="points",
                        to="players.player",
                    ),
                ),
            ],
            options={
                "unique_together": {("identifier", "player", "match")},
            },
        ),
    ]
