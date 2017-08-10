from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_legth = 250)
    slug = models.SlugField()
    Author = models.CharField(max_legth = 250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)