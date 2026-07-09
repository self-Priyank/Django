from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Student

def login_app(request):
    if request.method == "POST":
        U = request.POST.get("username")
        P = request.POST.get("password")
        user = authenticate(request, username=U, password=P)

        if user is not None and user.is_active and user.username == U:
            login(request, user)
            return redirect("app_1:student")            
        else:
            return render(request, "app_1/login.html", {"error": "Invalid username or password"})   
    
    return render(request, "app_1/login.html")

@login_required(login_url="login")
def student(request):
    all_students = Student.objects.all()
    return render(request, "app_1/student.html", {'students': all_students})

def logout_app(request):
    logout(request)
    return redirect("app_1:login")