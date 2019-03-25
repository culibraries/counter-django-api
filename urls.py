__author__ = 'mstacy'
from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from counter.views import PlatformViewSet, PlatformPublisherViewSet, PublisherViewSet

router = routers.SimpleRouter()
router.register('platforms', PlatformViewSet)
router.register('platformpublisher', PlatformPublisherViewSet)
router.register('publishers', PublisherViewSet)
# View
#router.register('vwsearch', VwSearchViewSet)
#router.register('vwsearchmv', VwSearchmvViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'jsonp', 'xml', 'yaml'])
