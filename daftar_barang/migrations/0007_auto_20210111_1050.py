# Generated by Django 2.2 on 2021-01-11 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_barang', '0006_barang_harga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='harga',
            field=models.IntegerField(null=True),
        ),
    ]
