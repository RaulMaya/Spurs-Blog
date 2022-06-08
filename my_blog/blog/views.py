from turtle import write_docstringdict
from django.shortcuts import render
from datetime import date
from django.db.models import Avg, Max, Min
from .models  import Post, Tag, Author
from django.shortcuts import render, get_object_or_404

# Create your views here.

def get_date(post):
    return post['date']

def starting_page(request):
    list_of_dicts = []
    posts = Post.objects.all().order_by("date")
    print(len(posts))
    print(posts[0].title, posts[0].author, posts[0].date)
    for post in posts:
        dictionary = {
          "slug": post.slug,
          "image": post.image_name,
          "author": post.author,
          "date": post.date,
          "title": post.title,
          "excerpt": post.excerpt,
          "content": post.content,
          "tag": post.tag
          }
        list_of_dicts.append(dictionary)

    sorted_posts = sorted(written_posts, key=get_date)
    latest_posts = list_of_dicts[-3:]
    return render(request, "blog/index.html", {"posts":latest_posts})

def posts(request):
    list_of_dicts = []
    posts = Post.objects.all().order_by("date")
    print(len(posts))
    print(posts[0].title, posts[0].author, posts[0].date)
    for post in posts:
        dictionary = {
          "slug": post.slug,
          "image": post.image_name,
          "author": post.author,
          "date": post.date,
          "title": post.title,
          "excerpt": post.excerpt,
          "content": post.content,
          "tag": post.tag
          }
        list_of_dicts.append(dictionary)
    sorted_posts = sorted(written_posts, key=get_date)
    return render(request, "blog/posts.html", {
        "all_posts":list_of_dicts
    })

def individual_post(request, slug):
    list_of_dicts = []
    posts = Post.objects.all().order_by("date")
    print(len(posts))
    print(posts[0].title, posts[0].author, posts[0].date)
    for post in posts:
        dictionary = {
          "slug": post.slug,
          "image": post.image_name,
          "author": post.author,
          "date": post.date,
          "title": post.title,
          "excerpt": post.excerpt,
          "content": post.content,
          "tag": post.tag
          }
        list_of_dicts.append(dictionary)
    selected_post = next(post for post in list_of_dicts if post['slug'] == slug)
    return render(request, "blog/individual_post.html", {
        "post": selected_post
    })