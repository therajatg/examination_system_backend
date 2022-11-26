from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=75)
    email=models.EmailField(null=False,blank=False,unique=True)
    isActive=models.BooleanField(default=True)
    Password=models.CharField(null=False,blank=False,max_length=20)

    def __str__(self):
        return self.Name

# class Student(models.Model):
#     student_id=models.AutoField(unique=True, primary_key=True)
#     name=models.CharField(max_length=50)
#     courses=models.ManyToManyField(Course)