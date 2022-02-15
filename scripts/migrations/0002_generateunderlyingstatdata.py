# Generated by Django 4.0.2 on 2022-02-12 13:49

import uuid

from django.db import migrations, models

import scripts.models.generate_underlying_stat_data


class Migration(migrations.Migration):

    dependencies = [
        ("scripts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GenerateUnderlyingStatData",
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
                    "ids",
                    models.TextField(
                        validators=[
                            scripts.models.generate_underlying_stat_data._validate_ids
                        ]
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Generate underlying stat data",
            },
        ),
    ]
