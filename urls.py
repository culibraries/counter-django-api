from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from counter.views import PlatformViewSet, PublisherViewSet, PublicationViewSet, TitleViewSet, FilterViewSet, StatsViewSet

router = routers.SimpleRouter()
router.register('platforms', PlatformViewSet, basename='platform')
router.register('publishers', PublisherViewSet, basename='publisher')
router.register('publications', PublicationViewSet, basename='publication')
router.register('titles', TitleViewSet, basename='title')
router.register('filters', FilterViewSet, basename='filter')
urlpatterns = router.urls
urlpatterns.append(
    path('static/', StatsViewSet.as_view(), name='static-view')
)
