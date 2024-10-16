# Generated by Django 5.1.1 on 2024-10-15 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_delete_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_phone_number',
            new_name='postal_code',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='additional_comments',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_county',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_postcode',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_street_address1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_street_address2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_town_or_city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='preferences',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='county_state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='street_address1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='street_address2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='town_city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
