# Generated by Django 5.1.1 on 2024-10-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0004_userprofile_first_name_userprofile_last_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="email",
            field=models.EmailField(default="default@example.com", max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="country",
            field=models.CharField(default="United Kingdom", max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="first_name",
            field=models.CharField(default="John", max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="last_name",
            field=models.CharField(default="Doe", max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="street_address1",
            field=models.CharField(default="Unknown", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="town_city",
            field=models.CharField(default="Unknown", max_length=50),
            preserve_default=False,
        ),
    ]
