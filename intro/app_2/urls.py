from . import views
from django.urls import path

urlpatterns = [
    path('student/', views.StudentView.as_view())
]