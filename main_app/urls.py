from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('games/', views.GameList.as_view(), name="game_list"),
    path('characters/', views.CharacterList.as_view(), name="character_list"),
    path('characters/new/', views.CharacterCreate.as_view(), name='character_create'),
    path('games/new/', views.GameCreate.as_view(), name='game_create'),
]