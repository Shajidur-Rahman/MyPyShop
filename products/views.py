from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
# Create your views here.

def hello(request):
    producte = Products.objects.all()
    return render(request, 'index.html')