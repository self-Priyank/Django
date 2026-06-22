from . import views
from django.urls import path

urlpatterns = [
    path('', views.login_app, name='login'),
    path('student/', views.student, name='student'),
    path('logout/', views.logout_app, name='logout'),
]