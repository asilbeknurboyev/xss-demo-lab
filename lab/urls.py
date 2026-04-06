from django.urls import path
from . import views

urlpatterns = [
    # Mana bu qator 'lab/' manzilini taniy oladi
    path('', views.index, name='index'), 
    
    path('reflected/', views.reflected_xss, name='reflected_xss'),
    path('stored/', views.stored_xss, name='stored_xss'),
]