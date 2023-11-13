from django.shortcuts import render, HttpResponse, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def Shopping(request):
    AllProducts = Product.objects.all()
    return render(request, 'index.html', {'Products' : AllProducts})

def About(request):
    return render(request, 'about.html')

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ("Login Successfully"))
            return redirect("home")
        else:
            messages.success(request, "Login Failed")
            return redirect("login")
    else:
        return render(request, "login.html")

def Logout(request):
    logout(request)
    messages.success(request, ("Logout Successfully"))
    return redirect("home")