from django.db import models

class Store(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(max_length=250,unique=True)
    password=models.CharField(max_length=51)
    cpassword=models.CharField(max_length=50)
# Create your models here.
