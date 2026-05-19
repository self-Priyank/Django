from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    email = models.EmailField()
    course = models.CharField(max_length=50)
