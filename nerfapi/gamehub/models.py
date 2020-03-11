from django.db import models

# Create your models here

class Team(models.Model):
    name = models.CharField(max_length=50)
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    created = models.DateTimeField(auto_now_add=True)


class Player(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    # XXX: only use cascade if you want to delte all the players when the Team is deleted
    # https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
    team = models.ForeignKey(Team, on_delete=models.CASCADE) 

    @property
    def team_name(self):
        return self.team.name