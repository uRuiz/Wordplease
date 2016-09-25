from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from posts.models import Post
from posts.serializers import PostSerializer, PostListSerializer


class PostListAPI(ListCreateAPIView):
    """
    Endpoint de listado y creación de posts
    """
    queryset = Post.objects.all()

    def get_serializer_class(self):
        return PostSerializer if self.request.method == 'POST' else PostListSerializer


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle, actualización y borrado de posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
