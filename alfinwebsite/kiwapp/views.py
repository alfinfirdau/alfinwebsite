from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())

def tentang(request):
    return render(request, 'tentang.html')

def kontak(request):
    return render(request, 'kontak.html')