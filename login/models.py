from django.db import models
# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=50, primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/users/', default="images/users/defaultUserImage.png", null=True)


class Seller(models.Model):
    email = models.EmailField(max_length=50, primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/sellers/', default="images/users/defaultSellerImage.png", null=True)
