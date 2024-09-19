from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=10)
    year = models.IntegerField(default=100)

class Author(models.Model):
    name = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)