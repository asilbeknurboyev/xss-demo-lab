from django.urls import path
from . import views

urlpatterns = [
    # Asosiy menyu (Dashboard)
    path('', views.index, name='index'), 
    
    # 3 ta zaiflik manzillari
    path('reflected/', views.reflected_view, name='reflected_view'),
    path('stored/', views.lab_view, name='stored_view'), 
    path('dom/', views.dom_view, name='dom_view'),
]
