from rest_framework import routers
from gamehub import views as api_views

router = routers.DefaultRouter()
router.register(r'status', api_views.StatusView)
router.register(r'players', api_views.PlayerViewset)
router.register(r'teams', api_views.TeamViewset)
