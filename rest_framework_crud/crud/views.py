from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import StudentSerializer, StudentClassSerializer, TrackSerializer, AlbumSerializer
from .models import student, studentClass, Track, Album
from django.http import HttpResponse
from .permissions import IsOwnerOrReadOnly
# Create your views here.


class studentViewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    # permission class (IsOwnerOrReadOnly) are used to update delete fields if it is creted by the same user
    permission_classes = [IsOwnerOrReadOnly]

    # this function are used to save student by login user only automatically
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class studentClassViewset(viewsets.ModelViewSet):
    queryset = studentClass.objects.all()
    serializer_class = StudentClassSerializer
    # permission class are used to create only if user is login
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # overiding create method for depth=1
    def create(self, request, *args, **kwargs):
        data = request.data
        new_studentClass = studentClass.objects.create(
            year = data['year'], 
            semester = data['semester'], 
            department = data['department'],
            student_id = data['student']
        )
        serilizer = StudentClassSerializer(new_studentClass)
        return Response(serilizer.data)

class trackViewset(viewsets.ModelViewSet):
    queryset = Track.objects.prefetch_related('album').all()
    serializer_class = TrackSerializer

class albumClassViewset(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

