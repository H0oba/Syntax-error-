from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Teacher, Attendance, Branch, Subject, Quiz, Score


def index(request):
    return render(request, 'stud.html', {
        'students': Student.objects.all(),
        'teachers': Teacher.objects.all(),
        'attendances': Attendance.objects.all(),
        'branches': Branch.objects.all(),
        'subjects': Subject.objects.all(),
        'quizzes': Quiz.objects.all(),
        'scores': Score.objects.all(),
    })
