from django.urls import path
from . import views

urlpatterns = [
    path('', views.lab_view, name='lab_view'),
]