from rest_framework import serializers
from .models import *


class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Publication
        fields = ('id', 'title', 'publisher', 'platform',
                  'print_issn', 'online_issn', 'period', 'journal_doi', 'proprietary_id', 'requests')


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Platform
        fields = ('id', 'name')


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Publisher
        fields = ('id', 'name')


class TitleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Title
        fields = ('id', 'title')
