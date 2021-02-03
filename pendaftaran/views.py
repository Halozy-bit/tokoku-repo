from django.shortcuts import render, redirect
from pendaftaran.models import Pelanggan
from pendaftaran.forms import FormPelanggan
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Berhasil membuat akun!")
            return redirect('signup')
        else:
            messages.error(request, "Gagal membuat akun!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        context = {
            'form' : form,
        }
    return render(request, 'pendaftaran/signup.html', context)


@login_required(login_url=settings.LOGIN_URL)
def pendaftaran(request):
    if request.POST:
        form = FormPelanggan(request.POST)
        if form.is_valid():
            form.save()
            form = FormPelanggan()

            context = { 
            'judul' : 'Pendaftaran',
            'subjudul' : 'MNUR',
            'form' : form,
            }
            return render (request, 'pendaftaran/profile.html', context)
    else:        
        form = FormPelanggan()
        context = {
            'judul' : 'Pendaftaran',
            'subjudul' : 'MNUR',
            'form' : form,
        }
    return render (request, 'pendaftaran/profile.html', context)
