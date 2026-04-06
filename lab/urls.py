from django.urls import path
from . import views

urlpatterns = [
    path('', views.lab_view, name='lab_view'), # Bu avvalgi Stored XSS uchun edi
    path('dom/', views.dom_view, name='dom_view'), # <-- MANA SHU QATORNI QO'SHDIK
]