from turtle import write_docstringdict
from django.shortcuts import render
from datetime import date

# Create your views here.
written_posts = [
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
    },
        {
        "slug":"liverpool_vs_real_madrid_final",
        "image":"ucl_liv_rfc.jpg",
        "author":"Raul Maya",
        "date":date(2021,12,25),
        "title":"Will Real Madrid get the 14th?",
        "excerpt":"Nkunku, Salah, Botman, Mane, Gnabry",
        "content": """

        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.
        
        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.
        
        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.""",
    },
        {
        "slug":"world_cup_qatar_winner",
        "image":"qatar.jpeg",
        "author":"Raul Maya",
        "date":date(2022,4,27),
        "title":"Favorites to be World Champions",
        "excerpt":"France, Brasil, Germany, Argentina, England",
        "content": """

        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.
        
        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.
        
        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.""",
    },
        {
        "slug":"erling_halaand",
        "image":"erling_halaand.jpg",
        "author":"Raul Maya",
        "date":date(2022,4,20),
        "title":"Erling Halaand a new Sky Blue",
        "excerpt":"Manchester City",
        "content": """

        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.
        
        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.
        
        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.""",
    },
        {
        "slug":"robert_lewandowski_issues",
        "image":"robert_lewandowski.jpg",
        "author":"Raul Maya",
        "date":date(2021,5,23),
        "title":"Robert Lewandowski seems to be leaving Bayern Munich",
        "excerpt":"Barcelona is pushing hard for the polish striker",
        "content": """

        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.
        
        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.
        
        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.""",
    },
        {
        "slug":"jose_mourinho_conference",
        "image":"mou_conference.jpg",
        "author":"Raul Maya",
        "date":date(2022,5,26),
        "title":"'The Special One' did it again!",
        "excerpt":"AS Roma crown as the first UEFA Conference League Champions",
        "content": """

        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.
        
        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.
        
        Even though in my opinion Real Madrid doesn't need to reinforce the attack, and I feel that Mbappe situation was all about
        bringing in a powerful and important name, Florentino must be looking for great names to bring in to Real Madrid.""",
    }
]
def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(written_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts":latest_posts})

def posts(request):
    sorted_posts = sorted(written_posts, key=get_date)
    return render(request, "blog/posts.html", {
        "all_posts":sorted_posts
    })

def individual_post(request, slug):
    selected_post = next(post for post in written_posts if post['slug'] == slug)
    return render(request, "blog/individual_post.html", {
        "post": selected_post
    })