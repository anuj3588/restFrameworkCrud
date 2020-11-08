from django.contrib import admin
from .models import student, studentClass,Track,Album
# Register your models here.

admin.site.register(studentClass)
admin.site.register(Track)
admin.site.register(Album)
admin.site.register(student)