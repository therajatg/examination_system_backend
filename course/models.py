from django.db import models
from staff.models import Staff
from student.models import Student

# Create your models here.


class Course(models.Model):
    Course_id= models.AutoField(primary_key=True)
    Name=models.CharField(blank=False,max_length=250,unique=True)
    Author=models.ForeignKey(Staff,on_delete=models.SET_NULL)

    def __str__(self):
        return self.Name

class Question(models.Model):
    Question_id=models.AutoField(primary_key=True)
    Question=models.TextField(max_length=500,blank=False,unique=True)
    Option1=models.CharField(max_length=250,blank=False)
    Option2=models.CharField(max_length=250,blank=False)
    Option3=models.CharField(max_length=250,blank=False)
    Option4=models.CharField(max_length=250,blank=False)
    Correct_Ans=models.CharField(max_length=250,blank=False)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.Question   

class Score(models.Model):
    Score_id=models.AutoField(primary_key=True)
    Score=models.IntegerField(blank=False,unique=True)
    Student_id=models.ForeignKey(Student,on_delete=models.SET_NULL,blank=False)
    Course_id=models.ForeignKey(Course,on_delete=models.CASCADE,blank=False)

    def __int__(self):
        return self.Score



# Course means test