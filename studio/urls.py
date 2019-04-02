from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, StudentViewSet, TeacherViewSet, DanceClassViewSet, JoinTeacherStudentViewSet

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'students', StudentViewSet, basename='student')
router.register(f'teachers', TeacherViewSet, basename='teacher')
router.register(f'classes', DanceClassViewSet, basename='dance_class')
router.register(f'join-teachers-students', JoinTeacherStudentViewSet, basename='join-teachers-students')

urlpatterns = router.urls