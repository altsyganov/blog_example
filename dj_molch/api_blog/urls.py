from .views import PostViewSet, TagViewSet
from rest_framework import renderers

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

tag_list = TagViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
tag_detail = TagViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
