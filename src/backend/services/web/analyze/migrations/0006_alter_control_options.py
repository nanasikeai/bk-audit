# Generated by Django 3.2.18 on 2023-06-01 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("analyze", "0005_auto_20230529_1701"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="control",
            options={
                "ordering": ["-priority_index", "control_type_id", "control_id"],
                "verbose_name": "Control",
                "verbose_name_plural": "Control",
            },
        ),
    ]
