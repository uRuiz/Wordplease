from django.shortcuts import render
from posts.models import Post


def home(request):
    """
    Renderiza el home con un listado de fotos
    :param request: objeto HttpRequest con los datos de la petición
    :return: objeto HttpResposne con los datos de la respuesta
    """
    posts = Post.objects.all().order_by('-created_at')  # Recupera todos los posts de la base de datos
    context = {'posts_list': posts[:5]}
    return render(request, 'posts/home.html', context)
