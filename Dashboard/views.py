from django.shortcuts import render
from .models import Student, Teacher, Attendance, Branch, Subject, Complaint

student_id = 1
student = Student.objects.get(id= student_id)
subjects = student.subjects.all()
attendance = student.attendance.all()

def index(request):
    return render(request, 'stud.html', {
        'students': Student.objects.all(),
        'teachers': Teacher.objects.all(),
        'attendances': Attendance.objects.all(),
        'branches': Branch.objects.all(),
        'subjects': Subject.objects.all(),
        'subjects_taken': subjects,
        'attendance': attendance,
    })

def submit_complaint(request, student):
    if request.method == 'POST':
        description_rec = request.POST['Complaint']

        new_complaint = Complaint(description = description_rec,student = student)
        new_complaint.save()

    return render(request, 'stud.html',{})
