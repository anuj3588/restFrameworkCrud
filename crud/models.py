from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()

class studentClass(models.Model):
    YEAR_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )

    SEMESTER_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
    )

    student = models.ForeignKey(student, on_delete=models.CASCADE)
    year = models.CharField(max_length=100, choices = YEAR_CHOICES)
    semester = models.CharField(max_length=100, choices = SEMESTER_CHOICES)
    department = models.CharField(max_length=100)
