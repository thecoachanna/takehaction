# Generated by Django 4.1.2 on 2022-10-15 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("disability_info", "0004_alter_user_disability_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="disability_description",
            field=models.TextField(default="", max_length=1000),
        ),
        migrations.AlterField(
            model_name="user",
            name="disability_name",
            field=models.CharField(default="", max_length=50),
        ),
    ]