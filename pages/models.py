'''from django.db import models''' #original content

# Create your models here.
from django.db import models


class Listing(models.Model):
    title = models.CharField(max_length=200)        # Doctor name
    location = models.CharField(max_length=100)     # Clinic location
    description = models.TextField(blank=True)      # Doctor bio
    
    def __str__(self):
        return self.title