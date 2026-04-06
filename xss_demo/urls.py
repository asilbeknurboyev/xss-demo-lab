from django.contrib import admin
from django.urls import path, include  # 'include' so'zini qo'shishni unutmang

urlpatterns = [
    path('admin/', admin.site.urls),
    # Bizning 'lab' ilovamizni butun loyihaga ulaymiz
    path('lab/', include('lab.urls')),
]