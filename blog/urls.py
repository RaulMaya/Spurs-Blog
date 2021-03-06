from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'starting_page'),
    path('posts', views.PostsView.as_view(), name = 'posts'),
    path('posts/<slug:slug>',views.DetailPostView.as_view(), name = 'individual_post'), #/posts/real-madrids-wild-cards
    path('read-later', views.ReadLaterView.as_view(), name ='read-later'),
    path('favorites', views.FavoritesView.as_view(), name ='favorites')
]