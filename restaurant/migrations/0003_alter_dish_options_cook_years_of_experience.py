# Generated by Django 4.1.3 on 2022-12-02 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0002_cook_position"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dish",
            options={"ordering": ["name"], "verbose_name_plural": "Dishes"},
        ),
        migrations.AddField(
            model_name="cook",
            name="years_of_experience",
            field=models.IntegerField(default=1),
        ),
    ]
