from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.urls import reverse
from django.utils import timezone

from posts.forms import PostForm
from posts.models import Post


class HomeView(View):

    def get(self, request):
        """
        Renderiza el home con un listado de fotos
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResposne con los datos de la respuesta
        """
        # Recupera todos los posts de la base de datos que se puedan mostrar
        posts = Post.objects.all().order_by('-created_at')
        if not request.user.is_authenticated():
            posts = posts.filter(published_date__lte=timezone.now())
        else:
            posts = posts.filter(Q(published_date__lte=timezone.now()) | Q(owner=request.user))

        context = {'posts_list': posts[:5]}
        return render(request, 'posts/home.html', context)


class PostQueryset(object):

    @staticmethod
    def get_posts_by_user(user):
        possible_posts = Post.objects.all().select_related('owner')
        if not user.is_authenticated():
            possible_posts = possible_posts.filter(published_date__lte=timezone.now())
        elif not user.is_superuser:
            possible_posts = possible_posts.filter(Q(published_date__lte=timezone.now()) | Q(owner=user))
        return possible_posts


class PostDetailView(View):

    def get(self, request, username, pk):
        """
        Renderiza el detalle de una imagen
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResposne con los datos de la respuesta
        """
        possible_posts = PostQueryset.get_posts_by_user(request.user).filter(pk=pk)
        if len(possible_posts) == 0:
            return HttpResponseNotFound("El post que buscas no existe")
        elif len(possible_posts) > 1:
            return HttpResponse("Múltiples opciones", status=300)
        post = possible_posts[0]
        context = {
            'post': post,
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


class BlogListView(View):

    def get(self, request):
        blog_list = User.objects.all()
        context = {
            'list': blog_list,
        }
        return render(request, 'posts/blogs_list.html', context)


class MyPostsListView(View):

    def get(self, request, username):
        my_posts_list = Post.objects.filter(owner=self.request.user).order_by('-published_date')
        context = {
            'posts_list': my_posts_list,
        }
        return render(request, 'posts/post_list.html', context)