from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=50, default='Unknown')
    course = models.CharField(max_length=50)
