from rest_framework import serializers

from .models import Announcement


class AnnouncementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'description']


class AnnouncementCreatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'description']


class AnnouncementRetrieveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'



class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'