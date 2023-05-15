from django.db import models
from django.core.validators import EmailValidator, MaxValueValidator, MinValueValidator

email_validator = EmailValidator(message='Please enter a valid email address.')
max_score = MaxValueValidator(
    100, message='Please enter a number less than 100')
min_score = MinValueValidator(0, message='Please enter a number above 0')


class Quiz(models.Model):
    score = models.IntegerField(validators=[max_score, min_score])


class Subject(models.Model):
    name = models.CharField(max_length=50)


class Branch(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)


class Attendance(models.Model):
    date = models.DateField()
    attended = models.BooleanField()

# Teacher Class


class Teacher(models.Model):

    GENDER_OPTIONS = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, options=GENDER_OPTIONS)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    email = models.EmailField(validators=[email_validator])
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)


# Student Class
class Student(models.Model):

    GENDER_OPTIONS = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, options=GENDER_OPTIONS)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    guardian_first_name = models.CharField(max_length=50)
    guardian_second_name = models.CharField(max_length=50)
    email = models.EmailField(validators=[email_validator])
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
