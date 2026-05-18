from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<body><h1 style='color:navy;'>Welcome to Django!</h1>" \
    "<p style='color:lime; font-size:24px;'> This is app_1 </p></body>")