from rest_framework import serializers
from . import models

class PlayerSerializer(serializers.ModelSerializer):
    #team_name = serializers.ReadOnlyField()

    class Meta:
        model = models.Player
        fields = ('id', 'name', 'created', 'team')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = ('id', 'name', 'created')
