from . import views
from django.urls import path

urlpatterns = [
    path('', views.login_app, name='login'),
    path('students/', views.students, name='students'),
]