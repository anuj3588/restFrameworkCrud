from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer, StudentClassSerializer
from .models import student, studentClass
from django.http import HttpResponse
# Create your views here.


class studentViewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class studentClassViewset(viewsets.ModelViewSet):
    queryset = studentClass.objects.all()
    serializer_class = StudentClassSerializer
