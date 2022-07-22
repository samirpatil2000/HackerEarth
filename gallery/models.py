from django.db import models

# Create your models here.
from django.urls import reverse
from utils.constant import URLS

class Image(models.Model):
    name = models.CharField(max_length=20, default="The Image")
    url = models.CharField(max_length=200)
    detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(URLS.IMAGE_DETAILS, kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse(URLS.UPDATE_IMAGE, kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse(URLS.DELETE_IMAGE, kwargs={'pk': self.id})
