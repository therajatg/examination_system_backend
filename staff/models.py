from django.db import models

# Create your models here.

class Staff(models.Model):
    staff_id=models.AutoField(unique=True, primary_key=True)
    name=models.models.CharField(max_length=50)
    