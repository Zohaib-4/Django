from django.db import models

class mydata(models.Model):
  fname = models.CharField(max_length=255)
  lname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  gender = models.CharField(max_length=255)
