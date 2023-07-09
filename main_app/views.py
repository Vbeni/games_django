from django.shortcuts import render, redirect
from django.views import View #view class to handle requests 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# import models
from .models import Game, Character, GameCollection
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# after our other imports 
from django.views.generic import DetailView


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gamecollection"] = GameCollection.objects.all()
        return context
    
class About(TemplateView):
    template_name = "about.html"

class GameList(TemplateView):
    template_name='game_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["games"] = Game.objects.filter(name__icontains=name)
        else:
            context["games"] = Game.objects.all()
            context["header"] = "Game List"
        return context

class CharacterCreate(CreateView):
    model = Character
    fields = ['name', 'image', 'bio']
    template_name = "character_create.html"
    success_url = "/characters/"

class GameCreate(CreateView):
    model = Game
    fields = ['name', 'image', 'description']
    template_name = "game_create.html"
    success_url = "/games/"

# class Game:
#     def __init__(self, name, image, description):
#         self.name = name
#         self.image = image
#         self.description = description

class CharacterList(TemplateView):
    template_name='character_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["characters"] = Character.objects.all() # this is where we add the key into our context object for the view to use
        return context

class CharacterDetail(DetailView):
    model = Character
    template_name = "character_detail.html"

class GameDetail(DetailView):
    model = Game
    template_name = "game_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gamecollections"] = GameCollection.objects.all()
        return context

class CharacterUpdate(UpdateView):
    model = Character
    fields = ['name', 'image', 'bio']
    template_name = "character_update.html"
    success_url = "/characters/"

class GameUpdate(UpdateView):
    model = Game
    fields = ['name', 'image', 'description']
    template_name = "game_update.html"
    success_url = "/games/"
class CharacterDelete(DeleteView):
    model = Character
    template_name = "character_delete_confirmation.html"
    success_url = "/characters/"
class GameDelete(DeleteView):
    model = Game
    template_name = "game_delete_confirmation.html"
    success_url = "/games/"

class GameCollectionGameAssoc(View):

    def get(self, request, pk, game_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the GameCollection by the id and
            # remove from the join table the given game_id
            GameCollection.objects.get(pk=pk).games.remove(game_pk)
        if assoc == "add":
            # get the GameCollection by the id and
            # add to the join table the given game_id
            GameCollection.objects.get(pk=pk).games.add(game_pk)
        return redirect('home')

# class Character:
#     def __init__(self, name, image, bio):
#         self.name= name
#         self.image = image 
#         self.bio = bio

# characters = [
#     Character("Mario", "https://www.giantbomb.com/a/uploads/scale_small/15/153607/2895175-mario%2013.png", "Mario is a fictional character in the Mario video game franchise, owned by Nintendo and created by Japanese video game designer Shigeru Miyamoto."),
#     Character("Sonic", "https://www.giantbomb.com/a/uploads/scale_small/46/462814/3182258-4728507772-latest", "Sonic the Hedgehog is the protagonist of the Sonic the Hedgehog video game series released by Sega, as well as numerous spin-off comics, animations, and other media."),
#     Character("Pac-Man", "https://www.giantbomb.com/a/uploads/scale_medium/2/25631/1546400-pacman_1.jpg", "Pac-Man is a character from the game series of the same name by Bandai Namco. He is considered one of the classics of the medium, virtually synonymous with video games."),
#     Character("Samus Aran", "https://www.giantbomb.com/a/uploads/scale_small/16/164924/3445907-2936872287-samus.png", "Samus Aran is the protagonist of the Metroid science fiction action-adventure game series by Nintendo."),
#     Character("Link", "https://www.giantbomb.com/a/uploads/scale_small/15/153607/3294276-link.png", "Link is the main protagonist of Nintendo's video game series The Legend of Zelda. He appears in several incarnations over the course of the games, and also features in other Nintendo media."),
#     Character("Mega Man", "https://www.giantbomb.com/a/uploads/original/9/99864/2598105-3819367226-MegaM.jpg", "Mega Man, known as Rockman in Japan, is the protagonist of the Mega Man series by Capcom."),
# ]

# games = [
#     Game("Super Mario 64", "https://images.igdb.com/igdb/image/upload/t_cover_big/co6cl1.png", 
#        "The first three dimensional entry in the Mario franchise, Super Mario 64 follows Mario as he puts his broadened 3D movement arsenal to use in order to rescue Princess Peach from the clutches of his arch rival Bowser. Mario has to jump into worlds-within-paintings ornamenting the walls of Peach's castle, uncover secrets and hidden challenges and collect golden stars as reward for platforming trials."),
#     Game("The Legend of Zelda",
#        "https://images.igdb.com/igdb/image/upload/t_cover_big/co1uii.png", 
#        "The Legend of Zelda is an action-adventure video game franchise created by Japanese game designers Shigeru Miyamoto and Takashi Tezuka. It is primarily developed and published by Nintendo."),
#     Game("Pac-Man", "https://images.igdb.com/igdb/image/upload/t_cover_big/co545c.png", 
#        "Pac-Man is a maze action game developed and released by Namco for arcades in 1980. The original Japanese title of Puck Man was changed to Pac-Man for international releases as a preventative measure against defacement of the arcade machines."),
#     Game("Donkey Kong 64",
#        "https://images.igdb.com/igdb/image/upload/t_cover_big/co289i.png", 
#        "Donkey Kong 64 is a 1999 adventure platform game developed by Rare and published by Nintendo for the Nintendo 64. It is the first Donkey Kong game to feature 3D gameplay."),
#     Game("Space Invaders",
#        "https://images.igdb.com/igdb/image/upload/t_cover_big/co55yj.png", 
#        "Space Invaders is a 1978 arcade game created by Tomohiro Nishikado. It was manufactured and sold by Taito in Japan, and licensed in the United States by the Midway division of Bally."),
#     Game("Street Fighter II",
#        "https://images.igdb.com/igdb/image/upload/t_cover_big/co606p.png", 
#        "Street Fighter II: The World Warrior is a competitive fighting game originally released for the arcades in 1991. It is the second installment in the Street Fighter series and the sequel to Street Fighter, released in 1987."),
# ]
