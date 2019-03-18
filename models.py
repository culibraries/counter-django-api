# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Platform(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'platform'


class PlatformPublisher(models.Model):
    id = models.IntegerField(primary_key=True)
    platform_id = models.IntegerField()
    publisher_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'platform_publisher'


class Publication(models.Model):
    id = models.IntegerField(primary_key=True)
    publisher_id = models.IntegerField()
    title = models.CharField(max_length=100)
    print_issn = models.CharField(max_length=10, blank=True, null=True)
    online_issn = models.CharField(max_length=10, blank=True, null=True)
    journal_doi = models.CharField(max_length=100, blank=True, null=True)
    proprietary_id = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'publication'


class Publisher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'publisher'


class PublisherTmp(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'publisher_tmp'


class UsageStats(models.Model):
    id = models.IntegerField(primary_key=True)
    publication_id = models.IntegerField()
    year = models.SmallIntegerField()
    month = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usage_stats'
