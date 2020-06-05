from django.db import models

# Create your models here.
class BlogProject(models.Model):

    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=200)
