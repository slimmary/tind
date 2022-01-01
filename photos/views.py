from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Photo
from .serializers import PhotoSerializer, PhotoBriefSerializer
from users.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoBriefSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_object(self):
        return get_object_or_404(Photo, pk=self.kwargs.get('photo_id'))
