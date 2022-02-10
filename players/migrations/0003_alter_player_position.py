# Generated by Django 4.0.2 on 2022-02-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0002_alter_player_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="position",
            field=models.IntegerField(
                choices=[
                    (1, "Goalkeeper"),
                    (2, "Defender"),
                    (3, "Midfielder"),
                    (4, "Forward"),
                ]
            ),
        ),
    ]
