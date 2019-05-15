from django.urls import path
from counter.views import PlatformViewSet, PublisherViewSet, PublicationViewSet, TitleViewSet, FilterViewSet, StatsViewSet

urlpatterns = [
    path('platforms/',
         PlatformViewSet.as_view({'get': 'list'}), name='platform-view'),
    path('publishers/',
         PublisherViewSet.as_view({'get': 'list'}), name='publisher-view'),
    path('publications/',
         PublicationViewSet.as_view({'get': 'list'}), name='publication-view'),
    path('titles/', TitleViewSet.as_view({'get': 'list'}), name='title-view'),
    path('filters/',
         FilterViewSet.as_view({'get': 'list'}), name='filter-view'),
    path('static/', StatsViewSet.as_view(), name='static-view')
]
