from django.db import models

# Create your models here.
class Student(models.Model):
    studentID=models.IntegerField()
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=40)