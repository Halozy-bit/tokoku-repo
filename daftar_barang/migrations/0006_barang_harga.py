# Generated by Django 2.2 on 2021-01-11 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_barang', '0005_auto_20210111_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='harga',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]