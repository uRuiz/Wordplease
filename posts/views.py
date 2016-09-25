from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView
from django.urls import reverse

from posts.forms import PostForm
from posts.models import Post


class HomeView(View):

    def get(self, request):
        """
        Renderiza el home con un listado de fotos
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResposne con los datos de la respuesta
        """
        # Recupera todos los posts de la base de datos
        posts = Post.objects.all().order_by('-created_at')  # filter(published_date < datetime.now())
        context = {'posts_list': posts[:5]}
        return render(request, 'posts/home.html', context)


class PostDetailView(View):

    def get(self, request, pk):
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


class PostCreationView(View):

    @method_decorator(login_required())
    def get(self, request):
        """
        Presenta el formulario para crear un post
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResposne con los datos de la respuesta
        """
        message = None
        post_form = PostForm()
        context = {
            'form': post_form,
            'message': message,
        }
        return render(request, 'posts/post_creation.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Presenta el formulario para crear un post y en caso de que la petición sea POST la valida y la crea en caso de que
        sea válida
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResposne con los datos de la respuesta
        """
        message = None
        post_with_user = Post(owner=request.user)
        post_form = PostForm(request.POST, instance=post_with_user)
        if post_form.is_valid():
            new_post = post_form.save()
            post_form = PostForm()
            message = 'Post creado satisfactoriamente <a href="{0}">Ver post</a>'.format(
                reverse('posts_detail', args=[new_post.pk])
            )

        context = {
            'form': post_form,
            'message': message,
        }
        return render(request, 'posts/post_creation.html', context)


class PostListView(LoginRequiredMixin, ListView):

    model = Post
    template_name = 'posts/post_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

