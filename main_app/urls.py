from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('games/', views.GameList.as_view(), name="game_list"),
    path('characters/', views.CharacterList.as_view(), name="character_list"),
    path('characters/new/', views.CharacterCreate.as_view(), name='character_create'),
    path('games/new/', views.GameCreate.as_view(), name='game_create'),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name="character_detail"),
    path('characters/<int:pk>/update',views.CharacterUpdate.as_view(), name="character_update"),
    path('characters/<int:pk>/delete',views.CharacterDelete.as_view(), name="character_delete"),
    path('games/<int:pk>/', views.GameDetail.as_view(), name="game_detail"),
    path('games/<int:pk>/update',views.GameUpdate.as_view(), name="game_update"),
    path('games/<int:pk>/delete',views.GameDelete.as_view(), name="game_delete"),
    path('game_collections/<int:pk>/games/<int:game_pk>/', views.GameCollectionGameAssoc.as_view(), name="gamecollection_game_assoc"),
    path('game_collections/<int:pk>/games/<int:game_pk>/add/', views.GameCollectionGameAssoc.as_view(), name="gamecollection_game_assoc_add"),
    # path('accounts/signup/', views.Signup.as_view(), name="signup"),
]