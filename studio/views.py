# from django.shortcuts import render
from .models import School, Student, Teacher, DanceClass, JoinClassesAndStudents
from .serializers import SchoolSerializer, StudentSerializer, TeacherSerializer, DanceClassSerializer, JoinClassesAndStudentsSerializer
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

class JoinClassesAndStudentsViewSet(viewsets.ModelViewSet):
    queryset = JoinClassesAndStudents.objects.all()
    serializer_class = JoinClassesAndStudentsSerializer