from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(label='Nombre de usuario')
    pwd = forms.CharField(label='Contraseña', widget=forms.PasswordInput())


class SignupForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    name = forms.CharField(label="Nombre")
    surname = forms.CharField(label="Apellido")
    email = forms.CharField(label="Email", widget=forms.EmailInput())
