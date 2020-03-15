from rest_framework import serializers
from . import models

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = ('id', 'name', 'gametype', 'status')

class GamePlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GamePlay
        fields = ('id', 'game_id', 'status','game_data')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = ('id', 'name', 'created', 'team')

# note how this one is extended from the base serializer, 
# we want to be able to show the members on a team in the form
class TeamSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Team
        fields = ('id', 'name', 'players', 'created')
