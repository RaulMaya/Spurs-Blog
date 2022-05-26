import re
from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/posts.html")

def individual_post(request):
    pass