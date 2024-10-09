# Generated by Django 5.1.1 on 2024-10-09 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking_total_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
