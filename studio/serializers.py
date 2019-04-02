from rest_framework import serializers
from .models import School, Student, Teacher, DanceClass, JoinTeacherStudent

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        # fields = ['id', 'name', 'email', 'address', 'phone_number', 'regular_class_price', 'private_class_price']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['id', 'school_id', 'first_name', 'last_name', 'email', 'address', 'phone_number', 'join_date']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
#         fields = ['id', 'school_id', 'first_name', 'last_name', 'email', 'address', 'phone_number', 'hourly_wage']

class DanceClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanceClass
        fields = '__all__'
        # fields = ['id', 'school_id', 'primary_teacher', 'dance_type', 'level', 'description', 'is_private']

class JoinTeacherStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinTeacherStudent
        fields = '__all__'