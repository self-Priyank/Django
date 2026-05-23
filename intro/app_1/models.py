from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=50)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.name
