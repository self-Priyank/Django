from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30, validators=[MinLengthValidator(2)])
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15)])
    email = models.EmailField()
    city = models.CharField(max_length=50)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.name
