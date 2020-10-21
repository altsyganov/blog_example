from django.test import TestCase

from .models import Post, Tag
    #
    #
    # path('posts/create/', PostCreate.as_view(), name='post_create_url'),
    # path('posts/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    # path('posts/<str:slug>/update', PostUpdate.as_view(), name='post_update_url'),
    # path('posts/<str:slug>/delete', PostDelete.as_view(), name='post_delete_url'),
    # path('tags/', tags_list, name='tags_list_url'),
    # path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
    # path('tags/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    # path('tags/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    # path('tags/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),


class test_Urls(TestCase):

    def test_root_redirect(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 301)

    def test_posts_page(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_tags_page(self):
        response = self.client.get('/blog/tags/')
        self.assertEqual(response.status_code, 200)

    def test_create_tag_page(self):
        response = self.client.get('/blog/tags/create/')
        self.assertEqual(response.status_code, 403)

    def test_create_post_page(self):
        response = self.client.get('/blog/posts/create/')
        self.assertEqual(response.status_code, 403)

    def test_post_detail_page(self):
        posts = Post.objects.all()
        for post in posts:
            response = self.client.get('/blog/posts/' + post.slug + '/')
            self.assertEqual(response.status_code, 200)
    def test_tag_detail_page(self):
        tags = Tag.objects.all()
        for tag in tags:
            response = self.client.get('blog/tags/' + tag.slug + '/')
            self.assertEqual(response.status_code, 200)
