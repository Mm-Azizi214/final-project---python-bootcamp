from django.db import models

# Create your models here.
class Criticism  (models.Model):
    moive_name= models.CharField(max_length=100)
    body=models.TextField()
    created=models.DateTimeField()