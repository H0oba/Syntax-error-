from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Quiz)
admin.site.register(Subject)
admin.site.register(Branch)
admin.site.register(Attendance)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Score)
admin.site.register(StudentLogin)
admin.site.register(TeacherLogin)
