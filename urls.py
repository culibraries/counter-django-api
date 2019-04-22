from rest_framework import routers
from counter.views import PlatformViewSet, PublisherViewSet, PublicationViewSet, TitleViewSet

router = routers.SimpleRouter()
router.register('platforms', PlatformViewSet, basename='platform')
router.register('publishers', PublisherViewSet, basename='publisher')
router.register('publications', PublicationViewSet, basename='publication')
router.register('titles', TitleViewSet, basename='title')
urlpatterns = router.urls
