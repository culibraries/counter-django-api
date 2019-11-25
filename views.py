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
# TODO check permission
# TODO add pagination

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


class PlatformViewSet(culibrariesTableViewSet):
    """

    Counter  Platform ViewSet with hyperlinked tables.

    """
    model = Platform
    serializer_class = PlatformSerializer

    def get_queryset(self):
        queryset = Platform.objects.all()
        key = self.request.query_params.get('key', None)
        filterType = self.request.query_params.get('type', 'is')
        if key is not None:
            if filterType == 'is':
                queryset = queryset.filter(name__icontains=key)
            if filterType == 'is_not':
                queryset = queryset.filter().exclude(name__icontains=key)
        return queryset


class BasicPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100000


class PublisherViewSet(culibrariesTableViewSet):
    """

    Counter Publisher ViewSet with hyperlinked tables.

    """
    model = Publisher
    serializer_class = PublisherSerializer

    def get_queryset(self):
        queryset = Publisher.objects.all()
        key = self.request.query_params.get('key', None)
        filterType = self.request.query_params.get('type', 'is')
        if key is not None:
            if filterType == 'is':
                queryset = queryset.filter(name__icontains=key)
            if filterType == 'is_not':
                queryset = queryset.filter().exclude(name__icontains=key)
        return queryset


class TitleViewSet(culibrariesTableViewSet):
    """

    Counter Title ViewSet with hyperlinked tables.

    """
    model = Title
    serializer_class = TitleSerializer

    def get_queryset(self):
        queryset = Title.objects.all()
        key = self.request.query_params.get('key', None)
        filterType = self.request.query_params.get('type', 'is')
        if key is not None:
            if filterType == 'is':
                queryset = queryset.filter(name__icontains=key)
            if filterType == 'is_not':
                queryset = queryset.filter().exclude(name__icontains=key)
        return queryset


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
            for p in tuple(publisher.split('|')):
                if not p:
                    valuef = tuple(p.split(','))[0]
                    typef = tuple(p.split(','))[1]
                    if typef == 'is':
                        queryset = queryset.filter(publisher=valuef)
                    if typef == 'is_not':
                        queryset = queryset.filter().exclude(publisher=valuef)
                    if typef == 'contains':
                        queryset = queryset.filter(publisher__icontains=valuef)
                    if typef == 'does_not_contains':
                        queryset = queryset.filter().exclude(publisher__icontains=valuef)
                    if typef == 'starts_with':
                        queryset = queryset.filter(
                            publisher__startswith=valuef)
                    if typef == 'ends_with':
                        queryset = queryset.filter(publisher__endswith=valuef)

        if 'title' in self.request.GET:
            title = self.request.GET['title']
            for p in tuple(title.split('|')):
                if not p:
                    valuef = tuple(p.split(','))[0]
                    typef = tuple(p.split(','))[1]
                    if typef == 'is':
                        queryset = queryset.filter(title=valuef)
                    if typef == 'is_not':
                        queryset = queryset.filter().exclude(title=valuef)
                    if typef == 'contains':
                        queryset = queryset.filter(title__icontains=valuef)
                    if typef == 'does_not_contains':
                        queryset = queryset.filter().exclude(title__icontains=valuef)
                    if typef == 'starts_with':
                        queryset = queryset.filter(
                            title__startswith=valuef)
                    if typef == 'ends_with':
                        queryset = queryset.filter(title__endswith=valuef)

        if 'platform' in self.request.GET:
            platform = self.request.GET['platform']
            for p in tuple(platform.split('|')):
                if not p:
                    valuef = tuple(p.split(','))[0]
                    typef = tuple(p.split(','))[1]
                    if typef == 'is':
                        queryset = queryset.filter(platform=valuef)
                    if typef == 'is_not':
                        queryset = queryset.filter().exclude(platform=valuef)
                    if typef == 'contains':
                        queryset = queryset.filter(platform__icontains=valuef)
                    if typef == 'does_not_contains':
                        queryset = queryset.filter().exclude(platform__icontains=valuef)
                    if typef == 'starts_with':
                        queryset = queryset.filter(
                            platform__startswith=valuef)
                    if typef == 'ends_with':
                        queryset = queryset.filter(platform__endswith=valuef)

        if 'range' in self.request.GET:
            rangeDate = tuple(self.request.GET['range'].split('|'))
            fromDate = rangeDate[0]
            toDate = rangeDate[1]
            queryset = queryset.filter(period__range=(fromDate, toDate))

        return queryset

    # filter_class = AcctaxFilter
# ***************************************** Counter DB Views ********************************************************
