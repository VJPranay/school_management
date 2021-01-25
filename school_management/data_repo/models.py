from django.db import models


# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=255)
    contact_number = models.BigIntegerField()
    address = models.TextField()

    def __str__(self):
        return self.student_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=255)
    contact_number = models.BigIntegerField()
    address = models.TextField()

    def __str__(self):
        return self.teacher_name


class Class(models.Model):
    standard = models.IntegerField()
    section = models.CharField(max_length=255)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    room_no = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.standard) + " | " + str(self.section)


class ClassStudent(models.Model):
    standard = models.ForeignKey(Class, on_delete=models.SET_NULL, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.standard) + " | " + str(self.student)


class Attendance(models.Model):
    class_student = models.ForeignKey(ClassStudent, on_delete=models.SET_NULL, blank=True, null=True)
    is_present = models.BooleanField()
    date = models.DateField()

    def __str__(self):
        return str(self.class_student) + " | " + str(self.is_present) + " | " + str(self.date)
