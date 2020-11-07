from rest_framework import serializers
from .models import student, studentClass


class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentClass
        fields = '__all__'
        depth = 1

class StudentSerializer(serializers.ModelSerializer):
    student_detail = StudentClassSerializer(read_only=True,many=True)
    class Meta:
        model = student
        fields = '__all__'

