from django.contrib.postgres.fields import JSONField
from django.db import models
import uuid

# Create your models here
class Game(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=50)
    game_type = (
        (0, "Single"),
        (1, "Multi"),
        (2, "Team"),
    )   
    gametype = models.IntegerField(choices=game_type, default=1)
    game_status = (
        (0, "Offline"),
        (1, "Online"),
        (99, "Out of Service"),
    )   
    status = models.IntegerField(choices=game_status, default=1)

    def __str__(self):
        return self.name


class GamePlay(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    game_status = (
        (0, "Scanned"),
        (1, "Queued"),
    )   
    status = models.IntegerField(choices=game_status, default=1)
    game_data = JSONField()
    

class Team(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=50)
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    id = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    # XXX: only use cascade if you want to delte all the players when the Team is deleted
    # https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE) 

    def __str__(self):
        return '%s: %s' % (self.id, self.name)