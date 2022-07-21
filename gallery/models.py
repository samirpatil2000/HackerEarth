from django.db import models

# Create your models here.
from django.urls import reverse


class Image(models.Model):

    name   = models.CharField(max_length=20, default="The Image")
    url    = models.CharField(max_length=200)
    detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.id})
