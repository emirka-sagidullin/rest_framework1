from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=20)
    annotation = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.DateField()

    def __str__(self):
        return self.name