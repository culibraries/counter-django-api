from rest_framework import serializers
import json
from .models import *
import os
import requests


class WritableJSONField(serializers.WritableField):
    def to_native(self, obj):
        return obj  # json.dumps(obj)

    def from_native(self, value):
        return value  # json.loads(value)


class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    # field_data = WritableJSONField()
    ID = serializers.CharField(source='id')

    class Meta:
        model = Publication
        fields = ('title', 'publisher', 'platform',
                  'print_issn', 'online_issn', 'period', 'journal_doi', 'proprietary_id', 'requests')
