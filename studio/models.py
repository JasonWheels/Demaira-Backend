from django.db import models
from django.utils import timezone

class School(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    phone_number = models.IntegerField()
    regular_class_price = models.DecimalField(max_digits=5, decimal_places=2)
    private_class_price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    student_first_name = models.CharField(max_length=255)
    student_last_name = models.CharField(max_length=255)
    parent_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    phone_number = models.IntegerField()
    join_date = models.DateField()

    def __str__(self):
        return self.title

class Teacher(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    phone_number = models.IntegerField()
    hourly_wage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.first_name 

class DanceClass(models.Model):
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    dance_type = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    description = models.TextField()
    is_private = models.BooleanField()

    def __str__(self):
        return self.name 

class JoinClassesAndStudents(models.Model):
    class_id = models.ForeignKey(DanceClass, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

# class ContactInfor(models.Model): 