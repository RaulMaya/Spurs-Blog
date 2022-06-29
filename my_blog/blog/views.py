from webbrowser import get
from django.shortcuts import render
from datetime import date
from django.db.models import Avg, Max, Min
from .models  import Post
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
# Create your views here.

class IndexView(ListView):
    template_name = "blog/index.html"
    model  = Post
    ordering = ['-date','title']
    context_object_name = 'posts'

    def get_queryset(self):
        query_set =  super().get_queryset()
        data = query_set[:3]
        return data

def get_date(post):
    return post['date']

#def starting_page(request):
#    latest_posts = Post.objects.all().order_by("-date")[:3]
#
    # sorted_posts = sorted(written_posts, key=get_date)
    # latest_posts = list_of_dicts[-3:]

#    return render(request, "blog/index.html", {"posts":latest_posts})

class PostsView(ListView):
    template_name = "blog/posts.html"
    model  = Post
    ordering = ['-date','title']
    context_object_name = 'all_posts'

#def posts(request):
#    list_of_dicts = []
#    posts = Post.objects.all().order_by("-date")

    # sorted_posts = sorted(written_posts, key=get_date)
#    return render(request, "blog/posts.html", {
#        "all_posts":posts
#    })

class DetailPostView(DetailView):
    template_name = "blog/individual_post.html"
    model  = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tag.all()
        return context

#def individual_post(request, slug):
#    selected_post = get_object_or_404(Post, slug=slug)
#    # posts = Post.objects.all().order_by("date")
#    # selected_post = next(post for post in posts if post.slug == slug)
#    return render(request, "blog/individual_post.html", {
#        "post": selected_post, "tags":selected_post.tag.all()
#    })