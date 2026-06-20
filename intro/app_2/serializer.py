from rest_framework import serializers
from app_1.models import Student

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"