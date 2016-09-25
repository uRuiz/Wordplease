from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from users.forms import LoginForm, SignupForm


class LoginView(View):

    def get(self, request):
        """
        Presenta el formulario de login
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResposne con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm()
        context = {'error': error_message, 'form': login_form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        """
        Gestiona el login de un usuario
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResposne con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_message = "Usuario o contraseña incorrecto"
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(request.GET.get('next', 'posts_home'))
                else:
                    error_message = "Cuenta de usuario desactivada"
        context = {'error': error_message, 'form': login_form}
        return render(request, 'users/login.html', context)


class LogoutView(View):

    def get(self, request):
        """
        Hace el logout de un usuario y redirige al login
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResposne con los datos de la respuesta
        """
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('posts_home')


class SignupView(View):

    def get(self, request):
        """
        Presenta el formulario de login
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResposne con los datos de la respuesta
        """
        error_message = ""
        signup_form = SignupForm()
        context = {'error': error_message, 'form': signup_form}
        return render(request, 'users/signup.html', context)

    def post(self, request):
        """
        Gestiona el login de un usuario
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResposne con los datos de la respuesta
        """
        error_message = ""
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data.get('username')
            password = signup_form.cleaned_data.get('password')
            name = signup_form.cleaned_data.get('name')
            surname = signup_form.cleaned_data.get('surname')
            email = signup_form.cleaned_data.get('email')
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=name,
                last_name=surname,
                email=email,
            )

        user.is_active = True
        user.save()
        context = {'error': error_message, 'form': signup_form}
        return render(request, 'users/login.html', context)
