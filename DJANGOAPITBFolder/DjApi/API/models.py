from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=45)
    title = models.CharField(max_length=100)
    numbers = models.IntegerField()

