# Generated by Django 2.2 on 2021-01-29 02:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('kota', models.CharField(max_length=255)),
                ('tanggal', models.DateField(default=datetime.date.today)),
                ('jalan', models.TextField()),
                ('rt', models.IntegerField()),
                ('rw', models.IntegerField()),
                ('pos', models.IntegerField()),
            ],
        ),
    ]