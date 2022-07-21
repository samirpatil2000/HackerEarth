from django.db import models

# Create your models here.

class Image(models.Model):

    name   = models.CharField(max_length=20, default="The Image")
    url    = models.CharField(max_length=200)
    detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
