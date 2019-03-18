from rest_framework import viewsets, filters, serializers
from rest_framework.renderers import BrowsableAPIRenderer, JSONPRenderer,JSONRenderer,XMLRenderer,YAMLRenderer

from counter.models import Platform,PlatformPublisher 


#************************************* Base Classes  ***************************************************************
class culibrariesTableViewSet(viewsets.ModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
#    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)

#DB View ViewSet Class
class culibrariesViewViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer) #,CSVRenderer)
#    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)

#***************************************** Counter Tables **********************************************************

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

#***************************************** Counter DB Views ********************************************************

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

#NOTES

#search_fields = ("sname","scientificnameauthorship","genus","species","subspecies","variety",
#                 "forma","elcode","iucncode","g_rank","s_rank","nativity","source","usda_code",
#                 "name","sspscientificnameauthorship","varscientificnameauthorship",
#                 "formascientificnameauthorship")
#ordering_fields = ("sname","scientificnameauthorship","family","genus","species","subspecies","variety",
#                 "forma","elcode","gelcode","iucncode","g_rank","s_rank","nativity","source","usda_code","tsn",
#                 "fed_status","st_status","swap","name","sspscientificnameauthorship","varscientificnameauthorship",
#                 "formascientificnameauthorship","tracked")
#

