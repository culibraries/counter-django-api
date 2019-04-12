__author__ = 'mstacy'
from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from counter.views import PlatformViewSet, PublisherViewSet, PublicationViewSet, TitleViewSet

router = routers.SimpleRouter()
router.register('platforms', PlatformViewSet)
router.register('publishers', PublisherViewSet)
router.register('publications', PublicationViewSet)
router.register('titles', TitleViewSet)
# View
#router.register('vwsearch', VwSearchViewSet)
#router.register('vwsearchmv', VwSearchmvViewSet)


urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       )
urlpatterns = format_suffix_patterns(
    urlpatterns, allowed=['api', 'json', 'jsonp', 'xml', 'yaml'])
