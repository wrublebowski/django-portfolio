from django.db import models

# Create your models here.
class PortfolioProject(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    # provide the direction     and pip install pillow
    image = models.ImageField(upload_to='portfolio/pictures/')
    url = models.URLField(blank=True)

    # to display titles in admin mode
    def __str__(self):
        return self.title
