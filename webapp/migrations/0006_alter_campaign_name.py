# Generated by Django 5.1.4 on 2024-12-13 02:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0005_remove_campaign_group_campaign_groups"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]