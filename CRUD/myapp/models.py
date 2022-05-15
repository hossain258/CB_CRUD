from django.db import models

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=30)
    student_roll= models.IntegerField()
    student_course =models.CharField(max_length=25)
    Title = models.CharField(max_length=30,blank=True)
    Description= models.CharField(max_length=1000,blank=True)
    
    

