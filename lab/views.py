from django.shortcuts import render, redirect
from .models import Izoh

def lab_view(request):
    # 1. Agar foydalanuvchi "Jo'natish" tugmasini bossa (POST so'rov)
    if request.method == 'POST':
        kiritilgan_matn = request.POST.get('xabar') # HTML'dagi input nomi 'xabar' bo'lishi kerak
        if kiritilgan_matn:
            # Matnni ma'lumotlar bazasiga saqlaymiz (Stored XSS uchun tayyorgarlik)
            Izoh.objects.create(matn=kiritilgan_matn)
        return redirect('/lab/') # Ma'lumot saqlangach, sahifani qayta yuklaymiz

    # 2. Bazada saqlangan barcha izohlarni o'qib olamiz
    barcha_izohlar = Izoh.objects.all().order_by('-vaqt')
    
    # 3. Ularni HTML sahifaga yuboramiz
# 3. Ularni HTML sahifaga yuboramiz
    return render(request, 'stored.html', {'izohlar': barcha_izohlar})
def dom_view(request):
    return render(request, 'dom.html')