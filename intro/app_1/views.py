from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from . import models

def login_app(request):
    if request.method == "POST":
        U = request.POST.get("username")
        P = request.POST.get("password")
        user = authenticate(request, username=U, password=P)
        
        if user is not None & user.is_active:
            if user.username != U:
                return render(request, "app_1/login.html", {"error": "Invalid username or password"})
            else:  
                login(request, user)
                return redirect("students")    
        else:
            return render(request, "app_1/login.html", {"error": "Invalid username or password"})   
    
    return render(request, "app_1/login.html")

def students(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    all_students = models.Student.objects.all()
    data = {'students': all_students}
    return render(request, "app_1/students.html", data)