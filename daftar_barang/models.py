from django.db import models
from datetime import date


class Jenis(models.Model):
    jenis = models.CharField(max_length=255)
    keterangan = models.TextField()

    def __str__(self):
        return self.jenis


class Barang(models.Model):
    nama_barang = models.CharField(max_length=255)
    kadaluarsa = models.DateField(auto_now_add=False, default=date.today)
    merk = models.CharField(max_length=255, null=True)
    harga = models.IntegerField(null=True)
    jenis = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)
    keterangan = models.TextField(null=True)

    def __str__(self):
        return self.nama_barang
