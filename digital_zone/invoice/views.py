from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'home/home.html')

def invoice(request):
    return render(request,'invoice/invoice.html')

def profile(request):
    return render(request,'profile/profile.html')

# Create your views here.
