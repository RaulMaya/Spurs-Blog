from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=15)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    author =  models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="post")
    image = models.ImageField(upload_to="images", null=True)
    date = models.DateField(auto_now_add=True) # Automatically set whenever there is an update
    slug = models.SlugField(max_length=100, unique=True, default="", db_index=True) # Unique True implies an index
    content = models.TextField(validators=[MinLengthValidator(10)])
    tag = models.ManyToManyField(Tag, null=False, related_name="posts")
    favorites = models.ManyToManyField(User, default=None, blank=True, related_name="favorites")
    readlater = models.ManyToManyField(User, default=None, blank=True, related_name="readlater")

    def get_absolute_url(self):
        return reverse("individual_post", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    user_name = models.CharField(max_length=75)
    user_email = models.EmailField()
    text =  models.TextField(max_length=400)
    date = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")


