# Generated by Django 5.1.1 on 2024-10-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yachts', '0005_yacht_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='yacht',
            name='detail_image',
            field=models.ImageField(blank=True, null=True, upload_to='yachts/details/'),
        ),
    ]