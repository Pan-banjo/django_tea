from django.contrib import admin

from .models import Teacher, Course, Student, TeacherAssistant


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["nickname","introduction","fans"]

# Register your models here.
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(TeacherAssistant)

