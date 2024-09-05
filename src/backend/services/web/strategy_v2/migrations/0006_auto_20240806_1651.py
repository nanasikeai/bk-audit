# Generated by Django 3.2.23 on 2024-08-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("strategy_v2", "0005_auto_20240802_0111"),
    ]

    operations = [
        migrations.AlterField(
            model_name="strategy",
            name="processor_groups",
            field=models.JSONField(blank=True, default=list, null=True, verbose_name="Processor"),
        ),
        migrations.AlterField(
            model_name="strategy",
            name="risk_title",
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name="Risk Title"),
        ),
    ]