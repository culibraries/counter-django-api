import django_filters
from django_filters import DateFilter

from django.forms.fields import MultipleChoiceField
from django_filters.filters import MultipleChoiceFilter
from .models import *


class MultipleField(MultipleChoiceField):
    def valid_value(self, value):
        return True


class MultipleFilter(MultipleChoiceFilter):
    field_class = MultipleField


class PublicationsFilter(django_filters.FilterSet):
    Publisher = MultipleFilter(lookup_type='in')
    Platform = MultipleFilter(lookup_type='in')
    # start_date = DateFilter(name='Period', lookup_type=('gt'),)
    # end_date = DateFilter(name='Period', lookup_type=('lt'))
    Title = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Publication
        fields = ['Title', 'Publisher', 'Platform']
