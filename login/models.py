from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

class Seller(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)