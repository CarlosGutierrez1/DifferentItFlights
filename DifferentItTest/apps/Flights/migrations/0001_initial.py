# Generated by Django 4.0.4 on 2022-04-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('numberFlightID', models.BigAutoField(primary_key=True, serialize=False)),
                ('departureTimestamp', models.CharField(max_length=100)),
                ('arrivalTimestamp', models.CharField(max_length=100)),
                ('departureIata', models.CharField(max_length=100)),
                ('arrivalIata', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Flight',
                'verbose_name_plural': 'Flights',
                'ordering': ['numberFlightID'],
            },
        ),
    ]
