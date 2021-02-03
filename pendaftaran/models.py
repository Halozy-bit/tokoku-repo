from django.db import models
from datetime import date

class Pelanggan(models.Model):
    nama = models.CharField(max_length=255)
    kota = models.CharField(max_length=255)
    tanggal = models.DateField(auto_now_add=False, default=date.today)
    jalan = models.TextField(null=False)
    rt = models.IntegerField(null=False)
    rw = models.IntegerField(null=False)
    pos = models.IntegerField(null=False)

    def __str_(self):
        return self.nama

