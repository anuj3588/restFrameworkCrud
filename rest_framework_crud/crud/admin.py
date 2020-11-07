from django.contrib import admin
from .models import student, studentClass
# Register your models here.

admin.site.register(studentClass)
admin.site.register(student)