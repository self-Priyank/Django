from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from . import models

def home(request):
    return HttpResponse("<body><h1 style='color:navy;'>Welcome to Django!</h1>" \
    "<p style='color:deeppink; font-size:24px;'> This is app_1 </p></body>")

def students(request):
    all_students = models.Student.objects.all()
    data = {'students': all_students}
    return render(request, 'students.html', data)