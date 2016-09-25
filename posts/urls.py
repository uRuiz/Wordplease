from django.conf.urls import url

from posts.api import PostListAPI
from posts.views import HomeView, PostDetailView, PostCreationView, BlogListView, MyPostsListView

urlpatterns = [
    url(r'^new_post$', PostCreationView.as_view(), name='posts_create'),
    url(r'^blogs/$', BlogListView.as_view(), name='blogs'),
    #url(r'^blogs/(?P<username>\w+)/$', MyPostsListView.as_view(), name='my_posts'),
    url(r'^blogs/(?P<username>\w+)/(?P<pk>\d+)$', PostDetailView.as_view(), name='posts_detail'),
    url(r'^$', HomeView.as_view(), name='posts_home'),

    # API URLs
    url(r'^api/1.0/posts/$', PostListAPI.as_view(), name='api_photos_list')
]
