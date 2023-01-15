from django.db import models

# Create your models here.

class NewApplication(models.Model):
    app_name = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    ip = models.CharField(max_length=15)
    date = models.CharField(max_length=8)
    pending_add = models.BooleanField()
    pending_delete = models.BooleanField()
    description = models.CharField(max_length=128)
