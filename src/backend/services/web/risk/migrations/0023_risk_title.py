# Generated by Django 3.2.23 on 2024-08-01 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("risk", "0022_risk_last_operate_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="risk",
            name="title",
            field=models.TextField(blank=True, default=None, null=True, verbose_name="Risk Title"),
        ),
    ]