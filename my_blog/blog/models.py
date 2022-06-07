from email.mime import image
from django.db import models

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=15)

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=30)
    excerpt = models.CharField(max_length=80)
    author =  models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="post")
    image_name = models.CharField(max_length=150)
    date = models.DateField()
    slug = models.SlugField(default="", blank=True, null = False, db_index=True)
    content = models.CharField(max_length=500)
    tag = models.ManyToManyField(Tag, null=False, related_name="post")


