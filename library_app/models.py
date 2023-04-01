from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
# Create your models here.

def tow_week_Later():
    return datetime.now() + timedelta(days=14)

class Book(models.Model):
    name=models.CharField(max_length=128)
    auther=models.CharField(max_length=128)
    isbn_number=models.PositiveBigIntegerField(unique=True)
    category=models.CharField(max_length=65)

    def __str__(self):
        return self.name + " , "+self.category


class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    classroom=models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=16, blank=True)
    image = models.ImageField(upload_to="", blank=True)

    def __str__(self):
        return str(self.user) + " ["+str(self.branch)+']' + " ["+str(self.classroom)+']' + " ["+str(self.roll_no)+']'


class IssuedBook(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=tow_week_Later())