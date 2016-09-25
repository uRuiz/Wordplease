from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posts.serializers import PostSerializer, PostListSerializer
from posts.views import PostQueryset


class PostListAPI(ListCreateAPIView):
    """
    Endpoint de listado y creación de posts
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return PostQueryset.get_posts_by_user(self.request.user)

    def get_serializer_class(self):
        return PostSerializer if self.request.method == 'POST' else PostListSerializer


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle, actualización y borrado de posts
    """
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return PostQueryset.get_posts_by_user(self.request.user)