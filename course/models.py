from django.db import models

# Create your models here.

class Course(models.Model):
    course_id=models.AutoField(unique=True, primary_key=True)
    name=models.CharField(max_length=100)