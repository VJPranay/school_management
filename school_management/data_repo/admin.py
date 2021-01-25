from django.contrib import admin
from .models import Student, Teacher, Class, ClassStudent, Attendance


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'blood_group', 'contact_number', 'date_of_birth']
    search_fields = ['student_name', 'contact_number']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_name', 'date_of_birth', 'blood_group', 'contact_number']
    search_fields = ['teacher_name', 'contact_number']


class ClassAdmin(admin.ModelAdmin):
    list_display = ['standard', 'section', 'class_teacher', 'room_no']


class ClassStudentAdmin(admin.ModelAdmin):
    list_display = ['standard', 'student']


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['class_student', 'is_present', 'date']


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(ClassStudent, ClassStudentAdmin)
admin.site.register(Attendance, AttendanceAdmin)
