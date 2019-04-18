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
from rest_framework import serializers


class Platform(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'platform'


class Publication(models.Model):
    ID = models.IntegerField()
    Title = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=100)
    Platform = models.CharField(max_length=100)
    PrintISSN = models.CharField(max_length=100)
    OnlineISSN = models.CharField(max_length=100)
    JournalDOI = models.CharField(max_length=100)
    ProprietaryID = models.CharField(max_length=100)
    Period = models.DateField()
    Total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'counter_result_detail'


class Title(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'publication'


class Publisher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    platform_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'publisher'
