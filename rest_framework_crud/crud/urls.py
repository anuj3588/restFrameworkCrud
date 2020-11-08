from django.urls import path, include
from rest_framework import routers
from .views import studentViewset,studentClassViewset, trackViewset, albumClassViewset

router = routers.DefaultRouter()
router.register('students', studentViewset, basename="students")
router.register('students-class', studentClassViewset, basename="students-class")
router.register('tarck', trackViewset, basename="tarck")
router.register('album', albumClassViewset, basename="album")

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
