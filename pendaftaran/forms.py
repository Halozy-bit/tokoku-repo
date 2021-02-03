from django.forms import ModelForm
from django import forms
from pendaftaran.models import Pelanggan

class FormPelanggan(ModelForm):
    class Meta:
        model = Pelanggan
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class' : 'form-control'}),
            'kota' : forms.TextInput({'class' : 'form-control'}),
            'tanggal' : forms.SelectDateWidget({'class' : 'form-control'}),
            'jalan' : forms.TextInput({'class' : 'form-control'}),
            'rt' : forms.NumberInput({'class' : 'form-control'}),
            'rw' : forms.NumberInput({'class' : 'form-control'}),
            'pos' : forms.NumberInput({'class' : 'form-control'}),
        }