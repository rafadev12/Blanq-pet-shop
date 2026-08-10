from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # O el nombre de tu función en views.py
]