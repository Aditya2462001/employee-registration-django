from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmployeeInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=490,null=True,blank=True)
    mname = models.CharField(max_length=50,null=True,blank=True)
    lname = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField( max_length=50,null=True,blank=True)
    number = models.CharField(max_length=10 ,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')


    def __str__(self):
        return self.fname
    

