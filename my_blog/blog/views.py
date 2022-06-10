from turtle import write_docstringdict
from xml.dom.minidom import Identified
from django.shortcuts import render
from datetime import date
from django.db.models import Avg, Max, Min
from .models  import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

def get_date(post):
    return post['date']

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]

    # sorted_posts = sorted(written_posts, key=get_date)
    # latest_posts = list_of_dicts[-3:]

    return render(request, "blog/index.html", {"posts":latest_posts})

def posts(request):
    list_of_dicts = []
    posts = Post.objects.all().order_by("-date")

    # sorted_posts = sorted(written_posts, key=get_date)
    return render(request, "blog/posts.html", {
        "all_posts":posts
    })

def individual_post(request, slug):
    selected_post = get_object_or_404(Post, slug=slug)
    # posts = Post.objects.all().order_by("date")
    # selected_post = next(post for post in posts if post.slug == slug)
    return render(request, "blog/individual_post.html", {
        "post": selected_post, "tags":selected_post.tag.all()
    })