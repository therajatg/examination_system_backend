from django.db import models
from course.models import Course

# Create your models here.

class Student(models.Model):
    student_id=models.AutoField(unique=True, primary_key=True)
    name=models.CharField(max_length=50)
    courses=models.ManyToManyField(Course)