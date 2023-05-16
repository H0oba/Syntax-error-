from django.db import models
from django.core.validators import EmailValidator, MaxValueValidator, MinValueValidator


email_validator = EmailValidator(message='Please enter a valid email address')

##############################################################################################
# Quiz Class "DONE"
##############################################################################################


class Quiz(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}"


##############################################################################################
# Subject Class "DONE"
##############################################################################################


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

##############################################################################################
# Branch Class "DONE"
##############################################################################################


class Branch(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

##############################################################################################
# Teahcer Class
##############################################################################################


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
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

##############################################################################################
# Student Class
##############################################################################################


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
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

##############################################################################################
# Attendance Class
##############################################################################################


class Attendance(models.Model):
    date = models.DateField(unique=True)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f"{self.date}"

##############################################################################################
# Scores Class "DONE"
##############################################################################################


class Score(models.Model):
    score = models.IntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)

    def __str__(self):
        return f"Quiz Name: {self.quiz.name}"
