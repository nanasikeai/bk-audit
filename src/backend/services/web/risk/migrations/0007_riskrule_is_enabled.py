# Generated by Django 3.2.18 on 2023-08-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("risk", "0006_init_security_person"),
    ]

    operations = [
        migrations.AddField(
            model_name="riskrule",
            name="is_enabled",
            field=models.BooleanField(default=True, verbose_name="Is Enabled"),
        ),
    ]
