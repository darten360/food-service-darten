# Generated by Django 4.1.3 on 2022-12-02 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0003_alter_dish_options_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.IntegerField(),
        ),
    ]
