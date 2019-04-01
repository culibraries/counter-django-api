from rest_framework import viewsets, filters, serializers, permissions
from rest_framework.renderers import BrowsableAPIRenderer, JSONPRenderer, JSONRenderer, XMLRenderer, YAMLRenderer
from counter.models import Platform, PlatformPublisher, Publisher, Publication
from filters import *
from serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
#from django_filters.rest_framework import DjangoFilterBackend

# ************************************* Base Classes  ***************************************************************


class culibrariesTableViewSet(viewsets.ModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,
                        JSONPRenderer, XMLRenderer, YAMLRenderer)
    # filter_backends = (filters.DjangoFilterBackend,
    #                   filters.SearchFilter, filters.OrderingFilter)

# DB View ViewSet Class


class culibrariesViewViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,
                        JSONPRenderer, XMLRenderer, YAMLRenderer)  # ,CSVRenderer)
#    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)

# ***************************************** Counter Tables **********************************************************


class PlatformViewSet(culibrariesTableViewSet):
    """

    Counter  Platform ViewSet with hyperlinked tables.

    """
    model = Platform
    queryset = Platform.objects.all()
    #serializer_class = AcctaxSerializer
    #filter_class = AcctaxFilter


class PlatformPublisherViewSet(culibrariesTableViewSet):
    """

    Counter PlatformPublisher ViewSet with hyperlinked tables.

    """
    model = PlatformPublisher
    queryset = PlatformPublisher.objects.all()
    #serializer_class = AcctaxSerializer
    #filter_class = AcctaxFilter


class PublisherViewSet(culibrariesTableViewSet):
    """

    Counter Publisher ViewSet with hyperlinked tables.

    """
    model = Publisher
    queryset = Publisher.objects.all()
    #serializer_class = AcctaxSerializer


class PublicationViewSet(culibrariesTableViewSet):
    """

    Counter Publication ViewSet with hyperlinked tables.

    """
    model = Publication
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = PublicationSerializer
    filter_class = PublicationsFilter
    queryset = Publication.objects.all()
    #filter_class = AcctaxFilter
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
