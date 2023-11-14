from django.urls import path
from .views import home,tentang,kontak


urlpatterns=[
    path('',home, name='home.html'),
    path('tentang',tentang, name='tentang.html'),
     path('kontak',kontak, name='kontak.html'),


]