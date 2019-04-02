from rest_framework import serializers
from .models import School, Student, Teacher, DanceClass, JoinClassesAndStudents

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        # fields = ['id', 'name', 'email', 'address', 'phone_number', 'regular_class_price', 'private_class_price', 'description']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['id', 'school_id', 'student_first_name', 'student_last_name', 'parent_name', 'email', 'address', 'phone_number', 'join_date']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        # fields = ['id', 'school_id', 'first_name', 'last_name', 'email', 'address', 'phone_number', 'hourly_wage']

class DanceClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanceClass
        fields = '__all__'
        # fields = ['id', 'school_id', 'teacher_id', 'dance_type', 'level', 'description', 'is_private']

class JoinClassesAndStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinClassesAndStudents
        fields = '__all__'