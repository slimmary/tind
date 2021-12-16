from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['user', 'name', 'birthday', 'age', 'gender', 'sex_orientation', 'about' ]


class UserProfileBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', 'gender', 'sex_orientation', 'age')