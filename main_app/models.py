from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=1024)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Character(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=1024)
    bio = models.TextField()
    games = models.ManyToManyField(Game, related_name='characters')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']