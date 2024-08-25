from django.db import models

class Users(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone= models.IntegerField(null=True)