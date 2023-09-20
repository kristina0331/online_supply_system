from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
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

    return render(request, 'accounts/User/dashboard.html', context)   

def requester(request,):
    requester = Requester.objects.all()
    context= {'requester': requester, 'products': products}
    return render(request, 'accounts/User/requester.html', context)

def products(request):
    products = Products.objects.all()   
    return render(request, 'accounts/User/products.html', {'products': products})

def status(request):
    
    return render(request, 'accounts/User/status.html') 

def homepage(request):
    return render(request, 'accounts/User/homepage.html')

def register(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact1 = request.POST['contact1']
        contact2 = request.POST['contact2']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account is successfully created.")

        return redirect('login')



    return render(request, 'accounts/User/register.html')

from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            auth_login(request, user)  # Use auth_login here to avoid conflicts
            fname = user.first_name
            return render(request, "accounts/User/requester.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('homepage')
    
    return render(request, 'accounts/User/login.html')



def signout(request):
    pass


