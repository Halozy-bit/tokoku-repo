# Generated by Django 2.2 on 2021-01-11 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_barang', '0007_auto_20210111_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jenis',
            old_name='nama_jenis',
            new_name='jenis',
        ),
    ]
