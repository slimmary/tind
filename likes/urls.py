from django.urls import path
from . import views


urlpatterns = [
    path('', views.LikeList.as_view(), name='like_list'),
    path('<int:like_id>', views.LikeDetail.as_view(), name='like'),

]