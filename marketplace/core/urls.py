from django.contrib import admin
from django.urls import path, include
from core.views import index, contacts

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts')
]