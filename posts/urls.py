from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from posts.api import PostViewSet
from posts.views import HomeView, PostDetailView, PostCreationView, BlogListView, MyPostsListView

router = DefaultRouter()
router.register('api/1.0/posts', PostViewSet, base_name='api_posts')

urlpatterns = [
    url(r'^new_post$', PostCreationView.as_view(), name='posts_create'),
    url(r'^blogs/$', BlogListView.as_view(), name='blogs'),
    url(r'^blogs/(?P<username>\w+)/(?P<pk>[0-9]+)$', PostDetailView.as_view(), name='posts_detail'),
    url(r'^blogs/(?P<username>\w+)/$', MyPostsListView.as_view(), name='my_posts'),
    url(r'^$', HomeView.as_view(), name='posts_home'),

    # API URLs
    url(r'', include(router.urls))
]
