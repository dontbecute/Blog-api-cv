from django.shortcuts import render
# Create your views here.
from rest_framework.generics import ListAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .serializers import PostSerializers
from Posts.models import Post
from .permission import IsAdminOrReadOnly

class PostListAPI(ListAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetalisAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

