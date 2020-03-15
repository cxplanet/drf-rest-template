from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

# Create your views here.
class StatusView(APIView):
    def get(self, request):
        content = {'status': 'ok'}
        return Response(content)

class GameViewset(viewsets.ModelViewSet):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer

class GamePlayViewset(viewsets.ModelViewSet):
    queryset = models.GamePlay.objects.all()
    serializer_class = serializers.GamePlaySerializer

class PlayerViewset(viewsets.ModelViewSet):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer

class TeamViewset(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

