from rest_framework.generics import ListCreateAPIView

from posts.models import Post
from posts.serializers import PostSerializer


class PostListAPI(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
