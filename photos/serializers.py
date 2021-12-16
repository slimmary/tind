from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'


class PhotoBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('image', 'user')