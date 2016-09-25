from django.conf.urls import url

from posts.views import HomeView, PostDetailView, PostCreationView, PostListView


urlpatterns = [
    url(r'^new_post$', PostCreationView.as_view(), name='posts_create'),
    url(r'^blogs/$', PostListView.as_view(), name='my_blog'),
    url(r'^blogs/(?P<username>\w+)/(?P<pk>\d+)$', PostDetailView.as_view(), name="posts_detail"),
    url(r'^$', HomeView.as_view(), name='posts_home'),
]
