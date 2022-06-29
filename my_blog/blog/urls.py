from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('posts', views.PostsView.as_view()),
    path('posts/<int:pk>', views.DetailPostView.as_view()), #/posts/real-madrids-wild-cards
]