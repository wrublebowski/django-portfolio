from django.db import models

# Create your models here.
class BlogProject(models.Model):

    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()

    # to display titles in admin mode
    def __str__(self):
        return self.title
