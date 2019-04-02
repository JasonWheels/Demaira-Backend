# from django.shortcuts import render
from .models import School, Student, Teacher, DanceClass, JoinTeacherStudent
from .serializers import SchoolSerializer, StudentSerializer, TeacherSerializer, DanceClassSerializer, JoinTeacherStudentSerializer
from rest_framework import viewsets

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class DanceClassViewSet(viewsets.ModelViewSet):
    queryset = DanceClass.objects.all()
    serializer_class = DanceClassSerializer

class JoinTeacherStudentViewSet(viewsets.ModelViewSet):
    queryset = JoinTeacherStudent.objects.all()
    serializer_class = JoinTeacherStudentSerializer