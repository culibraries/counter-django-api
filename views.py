from rest_framework import viewsets, filters
from rest_framework.renderers import BrowsableAPIRenderer, JSONPRenderer, JSONRenderer, XMLRenderer, YAMLRenderer
from counter.models import Platform, Publisher, Publication
# from .filter import PublicationsFilter
from serializers import PublicationSerializer
from rest_framework import permissions


# from django_filters.rest_framework import DjangoFilterBackend

# ************************************* Base Classes  ***************************************************************


class culibrariesTableViewSet(viewsets.ModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,
                        JSONPRenderer, XMLRenderer, YAMLRenderer)
    # filter_backends = (filters.DjangoFilterBackend,
    #                  filters.SearchFilter, filters.OrderingFilter)

# DB View ViewSet Class


class culibrariesViewViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,
                        JSONPRenderer, XMLRenderer, YAMLRenderer)  # ,CSVRenderer)
    filter_backends = (filters.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)

# ***************************************** Counter Tables **********************************************************


class PlatformViewSet(culibrariesTableViewSet):
    """

    Counter  Platform ViewSet with hyperlinked tables.

    """
    model = Platform
    queryset = Platform.objects.all()
    # serializer_class = AcctaxSerializer
    # filter_class = AcctaxFilter


class PublisherViewSet(culibrariesTableViewSet):
    """

    Counter Publisher ViewSet with hyperlinked tables.

    """
    model = Publisher
    queryset = Publisher.objects.all()
    # serializer_class = AcctaxSerializer


class PublicationViewSet(culibrariesViewViewSet):
    """

    Counter Publication ViewSet with hyperlinked tables.

    """
    model = Publication
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PublicationSerializer

    def get_queryset(self):
        queryset = Publication.objects.all()
        if 'publisher' in self.request.GET:
            publisher = self.request.GET['publisher']
            queryset = queryset.filter(
                Publisher__in=tuple(publisher.split('|')))
        if 'title' in self.request.GET:
            title = self.request.GET['title']
            queryset = queryset.filter(
                Title__contains=title
            )
        if 'platform' in self.request.GET:
            platform = self.request.GET['platform']
            queryset = queryset.filter(
                Platform__in=tuple(platform.split('|')))
        if 'range' in self.request.GET:
            rangeDate = tuple(self.request.GET['range'].split('|'))
            fromDate = rangeDate[0]
            toDate = rangeDate[1]
            queryset = queryset.filter(
                Period__range=(fromDate, toDate))

        return queryset

    # filter_class = AcctaxFilter
# ***************************************** Counter DB Views ********************************************************


"""

class VwSearchViewSet(culibrariesViewViewSet):
    ""
    This is the Search ViewSet with hyperlinked tables.
    ""
    model = VwSearch
    queryset = VwSearch.objects.all()
    search_fields = ()
    ordering_fields = ()

"""
