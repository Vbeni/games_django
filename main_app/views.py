from django.shortcuts import render
from django.views import View #view class to handle requests 
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"

class Games:
    def __init__(self, name, image, description):
        self.name = name
        self.image = image
        self.description = description

games = [
    
]
