# Generated by Django 2.2 on 2021-01-11 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_barang', '0008_auto_20210111_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='keterangan',
            field=models.TextField(null=True),
        ),
    ]
