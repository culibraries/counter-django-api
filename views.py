from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework_jsonp.renderers import JSONPRenderer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from counter.models import Platform, Publisher, Publication, Title, Filter
from counter.serializers import PublicationSerializer, PlatformSerializer, PublisherSerializer, TitleSerializer, FilterSerializer
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination


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
    # filter_backends = (filters.DjangoFilterBackend,
    #                    filters.SearchFilter, filters.OrderingFilter)

# ***************************************** Counter Tables **********************************************************


class PlatformViewSet(culibrariesTableViewSet):
    """

    Counter  Platform ViewSet with hyperlinked tables.

    """
    model = Platform
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class BasicPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100000


class PublisherViewSet(culibrariesTableViewSet):
    """

    Counter Publisher ViewSet with hyperlinked tables.

    """
    model = Publisher
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class TitleViewSet(culibrariesTableViewSet):
    """

    Counter Title ViewSet with hyperlinked tables.

    """
    model = Title
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class FilterViewSet(culibrariesTableViewSet):
    """

    Counter Filter ViewSet with hyperlinked tables.

    """
    model = Filter
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer


class StatsViewSet(APIView):
    """

    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        platform_count = Platform.objects.count()
        publisher_count = Publisher.objects.count()
        title_count = Title.objects.count()
        content = {
            'platform_count': platform_count,
            'publisher_count': publisher_count,
            'title_count': title_count
        }
        return Response(content)


class PublicationViewSet(culibrariesViewViewSet):
    """

    Counter Publication ViewSet with hyperlinked tables.

    """
    model = Publication
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PublicationSerializer
    pagination_class = BasicPagination

    def get_queryset(self):
        queryset = Publication.objects.all()
        if 'publisher' in self.request.GET:
            publisher = self.request.GET['publisher']
            queryset = queryset.filter(
                publisher__in=tuple(publisher.split('|')))
        if 'title' in self.request.GET:
            title = self.request.GET['title']
            queryset = queryset.filter(
                title__in=tuple(title.split('|')))
        if 'platform' in self.request.GET:
            platform = self.request.GET['platform']
            queryset = queryset.filter(
                platform__in=tuple(platform.split('|')))
        if 'range' in self.request.GET:
            rangeDate = tuple(self.request.GET['range'].split('|'))
            fromDate = rangeDate[0]
            toDate = rangeDate[1]
            queryset = queryset.filter(
                period__range=(fromDate, toDate))

        return queryset

    # filter_class = AcctaxFilter
# ***************************************** Counter DB Views ********************************************************
