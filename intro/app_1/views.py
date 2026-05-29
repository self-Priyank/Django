from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from . import models

def login_app(request):
    if request.method == "POST":
        return HttpResponse("Access denied")
    
    return render(request)

def students(request):
    if not request.user.is_active:
        return HttpResponse("Access denied")
    
    all_students = models.Student.objects.all()
    data = {'students': all_students}
    return render(request, 'students.html', data)