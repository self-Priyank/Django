from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import redirect
from .serializer import Student_serializer
from app_1.models import Student

class students_view(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_students = Student.objects.all()
        ser = Student_serializer(all_students, many = True)
        return Response(ser.data)