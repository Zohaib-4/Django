from django.db import models


class checkdb(models.Model):
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)

    