from django.shortcuts import render
from daftar_barang.models import Barang
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required(login_url=settings.LOGIN_URL)
def list(request):
    data = Barang.objects.all()
    context = {
        'judul': 'Daftar Barang',
        'subjudul': 'MNUR',
        'data': data,
    }
    return render(request, 'daftar_barang/index.html', context)
