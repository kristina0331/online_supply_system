from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')   

def contact(request):
    return render(request, 'accounts/about.html')

def pr(request):
    return render(request, 'accounts/purchase_request.html')

def tracker(request):
    return render(request, 'accounts/prtracker.html') 
