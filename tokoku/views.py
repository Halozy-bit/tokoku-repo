from django.shortcuts import render


def index(request):
    context = {
        'judul': 'Selamat Datang',
        'subjudul': 'MNUR',
    }
    return render(request, 'index.html', context)
