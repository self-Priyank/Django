from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='color:navy;'> Welcome to Django! <h1>")