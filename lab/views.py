from django.shortcuts import render, redirect
from .models import Izoh

# 1. BOSH SAHIFA (Asosiy menyu)
def index(request):
    return render(request, 'index.html')

# 2. REFLECTED XSS (Qidiruv tizimidagi zaiflik)
def reflected_view(request):
    kiritilgan_matn = request.GET.get('qidiruv', '')
    return render(request, 'reflected.html', {'matn': kiritilgan_matn})

# 3. STORED XSS (Ma'lumotlar bazasidagi zaiflik)
def lab_view(request):
    if request.method == 'POST':
        kiritilgan_matn = request.POST.get('xabar')
        if kiritilgan_matn:
            Izoh.objects.create(matn=kiritilgan_matn)
        return redirect('/lab/stored/') # Manzil endi stored bo'ldi
    
    barcha_izohlar = Izoh.objects.all().order_by('-vaqt')
    return render(request, 'stored.html', {'izohlar': barcha_izohlar})

# 4. DOM-BASED XSS (JavaScript zaifligi)
def dom_view(request):
    return render(request, 'dom.html')