from rest_framework import serializers
from .models import UserProfile
from photos.serializers import PhotoBriefSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    photo = PhotoBriefSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'name', 'birthday', 'age', 'gender', 'sex_orientation', 'about', 'photo' ]


class UserProfileBriefSerializer(serializers.ModelSerializer):
    photo = PhotoBriefSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('name', 'gender', 'sex_orientation', 'age', 'photo')