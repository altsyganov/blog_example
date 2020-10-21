from django.shortcuts import render, get_object_or_404

from rest_framework import permissions
from rest_framework.viewsets import  ModelViewSet

from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer


class PostViewSet(ModelViewSet):
    """

    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          ]


    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          ]
