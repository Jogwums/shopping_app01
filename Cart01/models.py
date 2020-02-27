from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Dposts(models.Model):
    firstname = models.CharField(max_length= 150)
    lastname = models.CharField(max_length= 150)
    

class shopProduct(models.Model):
    title = models.CharField(max_length=120, default = "Product Title")
    description = models.TextField(default = "Product Description")
    price = models.CharField(max_length=120, default = "00.00")
    Img = models.ImageField(default="True",upload_to ='images/')
    
class signUp(models.Model):
    username = models.CharField(max_length=120, default = "user name")
    password = models.CharField(max_length=50, default = "password")
    