from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User

email_validator = EmailValidator(message='Please enter a valid email address')

# Subject Class


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

# Branch Class


class Branch(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

# Teahcer Class


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
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name='teachers')
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

# Student Class


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
    subjects = models.ManyToManyField(Subject, related_name='students')
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT ,related_name='students')
    user = models.OneToOneField(User, null=True ,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.first_name} {self.second_name} ID: {self.pk}"

# Attendance Class


class Attendance(models.Model):
    date = models.DateField(unique=True)
    students = models.ManyToManyField(Student, related_name='attendance')

    def __str__(self):
        return f"{self.date}"

# Complaint Class

class Complaint(models.Model):
    description = models.CharField(max_length=1000)
    student = models.ForeignKey(Student, on_delete=models.PROTECT ,related_name='complaints')

    def __str__(self):
        return f"Complaint ({self.pk})"
