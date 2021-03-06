# Generated by Django 2.2 on 2021-01-11 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_barang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jenis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_jenis', models.CharField(max_length=255)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='barang',
            old_name='nama',
            new_name='nama_barang',
        ),
        migrations.AddField(
            model_name='barang',
            name='jenis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='daftar_barang.Jenis'),
        ),
    ]
