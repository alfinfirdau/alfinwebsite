from django.urls import path
from .views import home,keranjang,login,checkout,pesan


urlpatterns=[
    path('',home, name='home.html'),
    path('keranjang',keranjang, name='keranjang.html'),
    path('login',login, name='login.html'),
    path('checkout',checkout, name='checkout.html'),
    path('pesan',pesan, name='pesan.html'),
]