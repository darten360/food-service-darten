# Generated by Django 4.1.3 on 2022-11-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cook",
            name="position",
            field=models.CharField(default="Cook", max_length=30),
        ),
    ]
