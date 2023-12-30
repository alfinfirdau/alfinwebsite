from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())

def keranjang (request):
    return render(request, 'keranjang.html')

def login(request):
    return render(request, 'login.html')

def checkout(request):
    return render(request, 'checkout.html')

def pesan(request):
    return render(request, 'pesan.html')

