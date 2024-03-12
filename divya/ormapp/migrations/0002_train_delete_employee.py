# Generated by Django 5.0.2 on 2024-03-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_code', models.CharField(max_length=20)),
                ('train_name', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('start_station_code', models.CharField(max_length=20)),
                ('end_station_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
