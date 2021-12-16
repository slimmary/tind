from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Photo
from .serializers import PhotoSerializer, PhotoBriefSerializer


class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoBriefSerializer
    pagination_class = LimitOffsetPagination


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhotoSerializer

    def get_object(self):
        return get_object_or_404(Photo, pk=self.kwargs.get('photo_id'))



