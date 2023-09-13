from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    requester = Requester.objects.all()
    status = Status.objects.all()
    
    total_requester = requester.count()

    total_status = status.count()
    approved = status.filter(status='Approved').count()
    pending = status.filter(status='Pending').count()
    declined = status.filter(status='Declined').count()

    context = {'requester':requester, 'status': status, 
               'total_requester':  total_requester,
               'total_status': total_status,'approved': approved,
                 'pending': pending,'declined': declined}

    return render(request, 'accounts/dashboard.html', context)   

def requester(request,):
    requester = Requester.objects.all()
    context= {'requester': requester, 'products': products}
    return render(request, 'accounts/requester.html', context)

def products(request):
    products = Products.objects.all()   
    return render(request, 'accounts/products.html', {'products': products})

def status(request):
    
    return render(request, 'accounts/status.html') 
