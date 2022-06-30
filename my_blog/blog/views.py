from datetime import date
from multiprocessing import context
from django.db.models import Avg, Max, Min
from .models  import Post
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views import View
from .forms import CommentForm
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
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved = post_id in stored_posts
        else:
            is_saved = False

        return is_saved

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post":post,
            "tags":post.tag.all(),
            "comment_form": CommentForm(),
            "comments":post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/individual_post.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("individual_post", args=[slug]))

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


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "blog/stored-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])
        
        if post_id in stored_posts:
            stored_posts.remove(post_id)
            request.session["stored_posts"] = stored_posts
        else:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts
        


        return HttpResponseRedirect("/")