from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import redirect
from .serializer import StudentSerializer
from app_1.models import Student

class StudentView(GenericAPIView, ListModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

#   def get(self, request):
#       all_students = Student.objects.all()
#       ser = StudentSerializer(all_students, many = True)
#       return Response(ser.data)