from django.urls import path, include
from rest_framework import routers
from .views import studentViewset,studentClassViewset

router = routers.DefaultRouter()
router.register('students', studentViewset, basename="students")
router.register('students-class', studentClassViewset, basename="students-class")

urlpatterns = [
    path('', include(router.urls)),
]
