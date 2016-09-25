
from django.conf.urls import url

from posts.views import HomeView, PostDetailView, PostCreationView, PostListView


urlpatterns = [
    url(r'^new_post$', PostCreationView.as_view(), name='posts_create'),
    url(r'^posts/$', PostListView.as_view(), name='my_posts'),
    url(r'^blogs/(?P<pk>\d+)$', PostDetailView.as_view(), name="posts_detail"),
    url(r'^$', HomeView.as_view(), name='posts_home'),
]
