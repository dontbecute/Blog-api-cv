from django.urls import path 

from .views import PostListAPI , PostDetalisAPI


urlpatterns = [
    path('<int:pk>/' , PostDetalisAPI.as_view(), name='post_detalis'),
    path('' , PostListAPI.as_view() , name='post_list')
]