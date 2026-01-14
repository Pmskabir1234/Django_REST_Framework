from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=50)
    