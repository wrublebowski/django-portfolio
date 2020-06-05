from django.db import models

# Create your models here.
class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image1 = models.ImageField(upload_to='portfolio/pictures/')
    # provide the direction     and pip install pillow

    url = models.URLField(blank=True)
