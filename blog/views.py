from datetime import date
from gzip import READ
from multiprocessing import context
from this import d
from django.db.models import Avg, Max, Min
from .models  import Post
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views import View
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

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

class DetailPostView(View):
    #template_name = "blog/individual_post.html"
    #model  = Post

    def is_stored_post(self, request, post_id):
        if request.user.is_authenticated: 
            stored_posts = list(Post.objects.filter(readlater=request.user).values_list('pk', flat=True))

            if stored_posts is not None:
                is_saved = post_id in stored_posts
            else:
                is_saved = False

            return is_saved
        
        else:
            pass

    def favorites(self, request, post_id):
        if request.user.is_authenticated: 
            fav_post = list(Post.objects.filter(favorites=request.user).values_list('pk', flat=True))
            if fav_post is not None:
                is_fav = post_id in fav_post
            else:
                is_fav = False

            return is_fav

        else:
            pass

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post":post,
            "tags":post.tag.all(),
            "comment_form": CommentForm(),
            "comments":post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id),
            "favorite_one": self.favorites(request, post.id)
        }
        return render(request, "blog/individual_post.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        print(post)
        print(slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("blog:individual_post", args=[slug]))

        post = Post.objects.get(slug=slug)
        context = {
            "post":post,
            "tags":post.tag.all(),
            "comment_form": comment_form,
            "comments":post.comments.all().order_by("-id")
        }
        return render(request, "blog/individual_post.html", context)

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context["tags"] = self.object.tag.all()
    #    context["comment_form"] =  CommentForm()
    #    return context

#def individual_post(request, slug):
#    selected_post = get_object_or_404(Post, slug=slug)
#    # posts = Post.objects.all().order_by("date")
#    # selected_post = next(post for post in posts if post.slug == slug)
#    return render(request, "blog/individual_post.html", {
#        "post": selected_post, "tags":selected_post.tag.all()
#    })


class ReadLaterView(LoginRequiredMixin, View):

    def get(self, request):
        context = {}

        user_readlater = Post.objects.filter(readlater=request.user)

        if user_readlater is None or len(user_readlater) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            context["posts"] = user_readlater
            context["has_posts"] = True
        
        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        
        post_id = request.POST["post_id"]
        readlater_post = Post.objects.get(id__in=post_id)

        if readlater_post.readlater.filter(id=request.user.id).exists():
            readlater_post.readlater.remove(request.user)
        else:
            readlater_post.readlater.add(request.user)
        

        return HttpResponseRedirect("/")


class FavoritesView(LoginRequiredMixin, View):
    def get(self, request):
        context = {}

        user_favorites = Post.objects.filter(favorites=request.user)

        if user_favorites is None or len(user_favorites) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            context["posts"] = user_favorites
            context["has_posts"] = True
        
        return render(request, "blog/favorites.html", context)
    
    def post(self, request):

        post_id = request.POST["post_id"]
        favorite_post = Post.objects.get(id__in=post_id)

        if favorite_post.favorites.filter(id=request.user.id).exists():
            favorite_post.favorites.remove(request.user)
        else:
            favorite_post.favorites.add(request.user)
        

        return HttpResponseRedirect("/")