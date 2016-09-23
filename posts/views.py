from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from posts.models import Post


def home(request):
    """
    Renderiza el home con un listado de fotos
    :param request: objeto HttpRequest con los datos de la petición
    :return: objeto HttpResposne con los datos de la respuesta
    """
    # Recupera todos los posts de la base de datos
    posts = Post.objects.all().order_by('-created_at')  # filter(published_date < datetime.now())
    context = {'posts_list': posts[:5]}
    return render(request, 'posts/home.html', context)


def post_detail(request, pk):
    """
    Renderiza el detaller de una imagen
    :param request: objeto HttpRequest con los datos de la petición
    :return: objeto HttpResposne con los datos de la respuesta
    """
    possible_posts = Post.objects.filter(pk=pk).select_related('owner')
    if len(possible_posts) == 0:
        return HttpResponseNotFound("El post que buscas no existe")
    elif len(possible_posts) > 1:
        return HttpResponse("Múltiples opciones", status=300)
    post = possible_posts[0]
    context = {
        'post': post
    }

    return render(request, 'posts/post_detail.html', context)
