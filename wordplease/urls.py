"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from posts.views import HomeView, PostDetailView, PostCreationView, PostListView
from users.views import LoginView, LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),

    url(r'^new_post$', PostCreationView.as_view(), name='posts_create'),
    url(r'^posts/$', PostListView.as_view(), name='my_posts'),
    url(r'^blogs/(?P<pk>\d+)$', PostDetailView.as_view(), name="posts_detail"),
    url(r'^$', HomeView.as_view(), name='posts_home'),
]
