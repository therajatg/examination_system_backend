from django.db import models
# from course.models import Test

# Create your models here.


class Staff(models.Model):
    Staff_id = models.AutoField(primary_key=True)
    Name= models.CharField(max_length=75)
    Email=models.EmailField(null=False,blank=False,unique=True)
    Password=models.CharField(null=False,blank=False,max_length=20)

    def __str__(self):
        return self.Name

    