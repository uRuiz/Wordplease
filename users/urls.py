from django.conf.urls import url

from users.api import UserDetailAPI
from users.views import LoginView, LogoutView, SignupView

urlpatterns = [
    # Web URLs
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    url(r'^signup$', SignupView.as_view(), name='users_signup'),

    # API URLs
    url(r'api/1.0/users/(?P<pk>\d)$', UserDetailAPI.as_view(), name='api_user_list')
]
