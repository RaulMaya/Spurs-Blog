import re
from django.shortcuts import render
from datetime import date

# Create your views here.
posts = [
    {
        "slug":"real_madrid_decision",
        "image":"real_madrid_options.jpg",
        "author":"Raul Maya",
        "date":date(2022,5,27),
        "title":"Real Madrid Options To Mbappe News",
        "excerpt":"Nkunku, Salah, Botman, Mane, Gnabry",
        "content": """

        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.
        
        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.
        
        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.""",
    }
]

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/posts.html")

def individual_post(request, slug):
    return render(request, "blog/individual_post.html")