# Generated by Django 5.1.1 on 2024-10-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yachts', '0002_yacht_image_yacht_image_url_yacht_rating_yacht_sku_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yacht',
            name='sku',
        ),
        migrations.AlterField(
            model_name='yacht',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]