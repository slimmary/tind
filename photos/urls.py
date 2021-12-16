from django.urls import path
from . import views


urlpatterns = [
    path('', views.PhotoList.as_view(), name='photo_list'),
    path('<int:photo_id>', views.PhotoDetail.as_view(), name='photo'),

]