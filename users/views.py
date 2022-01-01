from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import UserProfile
from .serializers import UserProfileSerializer, UserProfileBriefSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileBriefSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return UserProfileSerializer
        return UserProfileBriefSerializer

    def get_object(self):
        return get_object_or_404(UserProfile, pk=self.kwargs.get('user_profile_id'))



