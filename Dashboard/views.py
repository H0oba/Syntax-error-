from django.shortcuts import render
from .models import Student, Teacher, Attendance, Branch, Subject, User


def dashboard(request, pk):
    
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    attendance = Attendance.objects.all()
    branch = Branch.objects.all()
    subjects = Subject.objects.all()
    user_log = User.objects.get(id=pk)
    
    student = students.get(user = user_log)
    subjects_taken = student.subjects.all()
    attendance_taken = student.attendance.all()

    context = {
        'students': students,
        'teachers': teachers,
        'attendances': attendance,
        'branches': branch,
        'subjects': subjects,
        'subjects_taken': subjects_taken,
        'attendance': attendance_taken,
        'student': student,
    }

    return render(request, 'stud.html', context)

#############################################################
