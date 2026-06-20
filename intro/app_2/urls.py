from . import views
from django.urls import path

urlpatterns = [
    path('students/', views.students_view.as_view())
]