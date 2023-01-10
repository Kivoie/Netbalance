from django.db import models

# Create your models here.

class NewApplication(models.Model):
    node_number = models.IntegerField()
    app_name = models.CharField(max_length=64)
    ip = models.CharField(max_length=15)
    date = models.CharField(max_length=8)
    description = models.CharField(max_length=128)
    
    #def __str__(self):
        #return str(self.node_number)