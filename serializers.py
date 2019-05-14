from rest_framework import serializers
from .models import *


class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Publication
        fields = ('id', 'title', 'publisher', 'platform',
                  'print_issn', 'online_issn', 'period', 'journal_doi', 'proprietary_id', 'requests')


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Platform
        fields = ('id', 'name')


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Publisher
        fields = ('id', 'name')


class TitleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Title
        fields = ('id', 'title')


class FilterSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(required=False)
    description = serializers.CharField(allow_blank=True)
    params = serializers.CharField(allow_blank=True)

    class Meta:
        model = Filter
        fields = ('id', 'name', 'description', 'params', 'owner',
                  'created_at', 'updated_at')
