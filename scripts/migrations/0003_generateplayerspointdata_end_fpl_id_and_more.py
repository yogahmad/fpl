# Generated by Django 4.0.2 on 2022-02-11 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scripts", "0002_generateplayerspointdata"),
    ]

    operations = [
        migrations.AddField(
            model_name="generateplayerspointdata",
            name="end_fpl_id",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="generateplayerspointdata",
            name="start_fpl_id",
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
