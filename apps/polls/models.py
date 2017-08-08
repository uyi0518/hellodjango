from django.db import models

# Create your models here.
class sign (models.Model):
    user = models.CharField(max_length=18)
    password=models.CharField(max_length=18)
    email= models.CharField(max_length=18)
    def __str__(self):
        return self.user