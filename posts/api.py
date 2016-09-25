from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from posts.models import Post
from posts.serializers import PostSerializer


class PostListAPI(ListCreateAPIView):
    """
    Endpoint de listado y creación de posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle, actualización y borrado de posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer