from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from . import models

def home(request):
    if request.user.is_active:
        return HttpResponse("<body><h1 style='color:navy;'>Welcome to Django!</h1>" \
        "<p style='color:deeppink; font-size:24px;'> This is app_1 </p></body>")
    
    return HttpResponse("Access denied")

def students(request):
    if not request.user.is_active:
        return HttpResponse("Access denied")
    
    all_students = models.Student.objects.all()
    data = {'students': all_students}
    return render(request, 'students.html', data)