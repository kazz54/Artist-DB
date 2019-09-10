from rest_framework import routers
from .api import ArtistsViewSet

router = routers.DefaultRouter()
router.register('artists', ArtistsViewSet, 'artist')

urlpatterns = router.urls
