from rest_framework import routers
from nerfapi.gamehub import views as api_views

router = routers.DefaultRouter()
router.register(r'games', api_views.GameViewset)
router.register(r'gameplay', api_views.GamePlayViewset)
router.register(r'players', api_views.PlayerViewset)
router.register(r'teams', api_views.TeamViewset)
