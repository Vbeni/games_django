from django.shortcuts import render
from django.views import View #view class to handle requests 
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"

class GameList(TemplateView):
    template_name='game_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = games # this is where we add the key into our context object for the view to use
        return context
    
class Game:
    def __init__(self, name, image, description):
        self.name = name
        self.image = image
        self.description = description

games = [
    Game("Super Mario 64", "https://images.igdb.com/igdb/image/upload/t_cover_big/co6cl1.png", 
       "The first three dimensional entry in the Mario franchise, Super Mario 64 follows Mario as he puts his broadened 3D movement arsenal to use in order to rescue Princess Peach from the clutches of his arch rival Bowser. Mario has to jump into worlds-within-paintings ornamenting the walls of Peach's castle, uncover secrets and hidden challenges and collect golden stars as reward for platforming trials."),
    Game("The Legend of Zelda",
       "https://images.igdb.com/igdb/image/upload/t_cover_big/co1uii.png", 
       "The Legend of Zelda is an action-adventure video game franchise created by Japanese game designers Shigeru Miyamoto and Takashi Tezuka. It is primarily developed and published by Nintendo."),
    Game("Pac-Man", "https://images.igdb.com/igdb/image/upload/t_cover_big/co545c.png", 
       "Pac-Man is a maze action game developed and released by Namco for arcades in 1980. The original Japanese title of Puck Man was changed to Pac-Man for international releases as a preventative measure against defacement of the arcade machines."),
    Game("Donkey Kong 64",
       "https://images.igdb.com/igdb/image/upload/t_cover_big/co289i.png", 
       "Donkey Kong 64 is a 1999 adventure platform game developed by Rare and published by Nintendo for the Nintendo 64. It is the first Donkey Kong game to feature 3D gameplay."),
    Game("Space Invaders",
       "https://images.igdb.com/igdb/image/upload/t_cover_big/co55yj.png", 
       "Space Invaders is a 1978 arcade game created by Tomohiro Nishikado. It was manufactured and sold by Taito in Japan, and licensed in the United States by the Midway division of Bally."),
    Game("Street Fighter II",
       "https://images.igdb.com/igdb/image/upload/t_cover_big/co606p.png", 
       "Street Fighter II: The World Warrior is a competitive fighting game originally released for the arcades in 1991. It is the second installment in the Street Fighter series and the sequel to Street Fighter, released in 1987."),
]
