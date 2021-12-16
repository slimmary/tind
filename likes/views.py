from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    pagination_class = LimitOffsetPagination


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LikeSerializer

    def get_object(self):
        return get_object_or_404(Like, pk=self.kwargs.get('like_id'))



