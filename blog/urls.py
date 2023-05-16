from django.urls import path
from .views import (
    PostDetailView,
    PostDeleteView,
    play_game,
)
from . import views 

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('games/<int:game_id>/', play_game, name='play_game'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
