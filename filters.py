import django_filters

from models import *


class PublicationsFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    publisher_id = django_filters.CharFilter(lookup_type='iexact')
    title = django_filters.CharFilter(lookup_type='iexact')
    is_active = django_filters.NumberFilter()

    class Meta:
        model = Publication
        fields = ['id', 'publisher_id', 'title', 'is_active']
