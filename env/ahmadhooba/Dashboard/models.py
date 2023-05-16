from django.db import models
from django.core.validators import EmailValidator, MaxValueValidator, MinValueValidator


email_validator = EmailValidator(message='Please enter a valid email address')
max_score = MaxValueValidator(
    100, message='Please enter a number less than 100')
min_score = MinValueValidator(0, message='Please enter a number above 0')


class Quiz(models.Model):
    number = models.IntegerField(default=0)
    score = models.IntegerField(validators=[max_score, min_score])
    students = models.ForeignKey(
        'Student', on_delete=models.PROTECT, default=None)

    def __str__(self):
        return f"Quiz {self.number}"


class Subject(models.Model):
    name = models.CharField(max_length=50)
    teachers = models.ForeignKey(
        'Teacher', on_delete=models.PROTECT, default=None)
    students = models.ForeignKey(
        'Student', on_delete=models.PROTECT, default=None)
    quizzes = models.ForeignKey('Quiz', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.name}"


class Branch(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    teachers = models.ForeignKey(
        'Teacher', on_delete=models.PROTECT, default=None)
    students = models.ForeignKey(
        'Student', on_delete=models.PROTECT, default=None)

    def __str__(self):
        return f"{self.name}"


class Teacher(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_OPTIONS = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    ]

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=1, choices=GENDER_OPTIONS, default=GENDER_MALE)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    email = models.EmailField(validators=[email_validator])

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Student(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_OPTIONS = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    ]

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=1, choices=GENDER_OPTIONS, default=GENDER_MALE)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    guardian_first_name = models.CharField(max_length=50)
    guardian_second_name = models.CharField(max_length=50)
    email = models.EmailField(validators=[email_validator])

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Attendance(models.Model):
    date = models.DateField()
    attended = models.BooleanField(default=False)
    students = models.ForeignKey(
        Student, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return f"{self.date}"
