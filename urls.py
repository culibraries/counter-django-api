from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from counter.views import PlatformViewSet, PublisherViewSet, PublicationViewSet, TitleViewSet

router = routers.SimpleRouter()
router.register('platforms', PlatformViewSet, basename='platform')
router.register('publishers', PublisherViewSet, basename='publisher')
router.register('publications', PublicationViewSet, basename='publication')
router.register('titles', TitleViewSet, basename='title')
urlpatterns = router.urls

# # View
# #router.register('vwsearch', VwSearchViewSet)
# #router.register('vwsearchmv', VwSearchmvViewSet)


# urlpatterns = patterns('',
#                        url(r'^', include(router.urls)),
#                        )
# urlpatterns += staticfiles_urlpatterns()

# urlpatterns = [
#     path('platforms/', PlatformViewSet.as_view(), name='platform-list'),
#     path('titles/', TitleViewSet.as_view(), name='title-list'),
#     path('publishers/', PublisherViewSet.as_view(), name='publisher-list'),
#     path('publications/', PublicationViewSet.as_view(), name='publication-list'),

# ]

# urlpatterns = format_suffix_patterns(
#     urlpatterns, allowed=['api', 'json', 'jsonp', 'xml', 'yaml'])
