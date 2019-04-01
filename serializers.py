from rest_framework import serializers
import json
from models import *
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
    field_data = WritableJSONField()
    id = serializers.CharField(source='id')

    class Meta:
        model = Publication
        fields = ('publisher_id', 'title', 'print_issn', 'proprietary_id'
                  'online_issn', 'journal_doi', 'is_active')
