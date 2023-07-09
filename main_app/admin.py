from django.contrib import admin
from .models import Game, Character, GameCollection

admin.site.register(Game) 
admin.site.register(Character) 
admin.site.register(GameCollection)