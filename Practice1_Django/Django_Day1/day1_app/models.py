from django.db import models

class new_table(models.Model):
  fname = models.CharField(max_length=255)
  lname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)