from django.shortcuts import render, redirect, get_object_or_404
from .models import Inscription
from .forms import InscriptionForm
from qr_code.qrcode.utils import QRCodeOptions

def inscription_create(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            inscription = form.save()
            return redirect('inscription_detail', inscription.id)
    else:
        form = InscriptionForm()
    return render(request, 'inscription_form.html', {'form': form})

def inscription_detail(request, pk):
    inscription = get_object_or_404(Inscription, pk=pk)
    qr_options = QRCodeOptions(size='M', border=6, error_correction='L')
    return render(request, 'inscription_detail.html', {'inscription': inscription, 'qr_options': qr_options})
