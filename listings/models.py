from django.db import models

# Create your models here.
from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()