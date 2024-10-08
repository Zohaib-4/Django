from django.db import models


class checkdb(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # It is recommended to hash passwords before saving.

    def __str__(self):
        return self.name