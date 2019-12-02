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
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permission import IsAdmin


class culibrariesTableViewSet(viewsets.ModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,
                        JSONPRenderer, XMLRenderer, YAMLRenderer)


class culibrariesViewViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,
                        JSONPRenderer, XMLRenderer, YAMLRenderer)  # ,CSVRenderer)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100000


class PlatformViewSet(culibrariesTableViewSet):
    """

    Counter  Platform ViewSet with hyperlinked tables.

    """
    # permission_classes = (IsAuthenticated, IsAdmin)
    http_method_names = ['get']

    model = Platform
    serializer_class = PlatformSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = Platform.objects.all()
        key = self.request.query_params.get('key', None)
        queryset = queryset.filter(name__icontains=key)
        return queryset


class PublisherViewSet(culibrariesTableViewSet):
    """

    Counter Publisher ViewSet with hyperlinked tables.

    """
    # permission_classes = (IsAuthenticated, IsAdmin)
    http_method_names = ['get']

    model = Publisher
    serializer_class = PublisherSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = Publisher.objects.all()
        key = self.request.query_params.get('key', None)
        queryset = queryset.filter(name__icontains=key)
        return queryset


class TitleViewSet(culibrariesTableViewSet):
    """

    Counter Title ViewSet with hyperlinked tables.

    """
    # permission_classes = (IsAuthenticated, IsAdmin)
    http_method_names = ['get']

    model = Title
    serializer_class = TitleSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = Title.objects.all()
        key = self.request.query_params.get('key', None)
        queryset = queryset.filter(title__icontains=key)
        return queryset


class FilterViewSet(culibrariesTableViewSet):
    """

    Counter Filter ViewSet with hyperlinked tables.

    """
    # permission_classes = (IsAuthenticated, IsAdmin)

    model = Filter
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer


class StatsViewSet(APIView):
    """

    """
    # permission_classes = (IsAuthenticated, IsAdmin)
    http_method_names = ['get']

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
    # permission_classes = (IsAuthenticated, IsAdmin)

    model = Publication
    serializer_class = PublicationSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        queryset = Publication.objects.all()
        if 'platform' in self.request.GET:
            platform = self.request.GET['platform']
            typeList = []
            valueList = []
            for p in tuple(platform.split('|')):
                typeList.append(tuple(p.split('*.'))[0])
                valueList.append(tuple(p.split('*.'))[1])
            if (len(set(typeList)) == 1):
                if typeList[0] == 'is':
                    queryset = queryset.filter(platform__in=valueList)
                if typeList[0] == 'is_not':
                    queryset = queryset.filter().exclude(platform__in=valueList)
                if typeList[0] == 'contains':
                    queryset = queryset.filter(
                        platform__icontains__in=valueList)
                if typeList[0] == 'does_not_contains':
                    queryset = queryset.filter().exclude(platform__icontains__in=valueList)
                if typeList[0] == 'starts_with':
                    queryset = queryset.filter(
                        platform__istartswith__in=valueList)
                if typeList[0] == 'ends_with':
                    queryset = queryset.filter(
                        platform__iendswith__in=valueList)
            for p in tuple(platform.split('|')):
                valuef = tuple(p.split('*.'))[1]
                typef = tuple(p.split('*.'))[0]
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
                        platform__istartswith=valuef)
                if typef == 'ends_with':
                    queryset = queryset.filter(platform__iendswith=valuef)

        if 'publisher' in self.request.GET:
            publisher = self.request.GET['publisher']
            typeList = []
            valueList = []
            for p in tuple(publisher.split('|')):
                typeList.append(tuple(p.split('*.'))[0])
                valueList.append(tuple(p.split('*.'))[1])
            if (len(set(typeList)) == 1):
                if typeList[0] == 'is':
                    queryset = queryset.filter(publisher__in=valueList)
                if typeList[0] == 'is_not':
                    queryset = queryset.filter().exclude(publisher__in=valueList)
                if typeList[0] == 'contains':
                    queryset = queryset.filter(
                        publisher__icontains__in=valueList)
                if typeList[0] == 'does_not_contains':
                    queryset = queryset.filter().exclude(publisher__icontains__in=valueList)
                if typeList[0] == 'starts_with':
                    queryset = queryset.filter(
                        publisher__istartswith__in=valueList)
                if typeList[0] == 'ends_with':
                    queryset = queryset.filter(
                        publisher__iendswith__in=valueList)
            else:
                for p in tuple(publisher.split('|')):
                    valuef = tuple(p.split('*.'))[1]
                    typef = tuple(p.split('*.'))[0]
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
                            publisher__istartswith=valuef)
                    if typef == 'ends_with':
                        queryset = queryset.filter(publisher__iendswith=valuef)

        if 'title' in self.request.GET:
            title = self.request.GET['title']
            typeList = []
            valueList = []
            for p in tuple(publisher.split('|')):
                typeList.append(tuple(p.split('*.'))[0])
                valueList.append(tuple(p.split('*.'))[1])
            if (len(set(typeList)) == 1):
                if typeList[0] == 'is':
                    queryset = queryset.filter(title__in=valueList)
                if typeList[0] == 'is_not':
                    queryset = queryset.filter().exclude(title__in=valueList)
                if typeList[0] == 'contains':
                    queryset = queryset.filter(
                        title__icontains__in=valueList)
                if typeList[0] == 'does_not_contains':
                    queryset = queryset.filter().exclude(title__icontains__in=valueList)
                if typeList[0] == 'starts_with':
                    queryset = queryset.filter(
                        title__istartswith__in=valueList)
                if typeList[0] == 'ends_with':
                    queryset = queryset.filter(
                        title__iendswith__in=valueList)
            for p in tuple(title.split('|')):
                valuef = tuple(p.split('*.'))[1]
                typef = tuple(p.split('*.'))[0]
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
                        title__istartswith=valuef)
                if typef == 'ends_with':
                    queryset = queryset.filter(title__iendswith=valuef)

        if 'range' in self.request.GET:
            rangeDate = tuple(self.request.GET['range'].split('|'))
            fromDate = rangeDate[0]
            toDate = rangeDate[1]
            queryset = queryset.filter(period__range=(fromDate, toDate))

        return queryset
