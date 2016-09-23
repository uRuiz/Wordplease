from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(label='Nombre de usuario')
    pwd = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
