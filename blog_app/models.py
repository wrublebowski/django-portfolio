from django.db import models

# Create your models here.
class BlogProject(models.Model):

    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=10000)

    # to display titles in admin mode
    def __str__(self):
        return self.title
