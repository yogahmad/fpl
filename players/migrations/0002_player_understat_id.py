# Generated by Django 4.0.2 on 2022-02-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="understat_id",
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]