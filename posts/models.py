from django.contrib.auth.models import User
from django.db import models

from categories.models import Category


class Post(models.Model):

    owner = models.ForeignKey(User)

    title = models.CharField(max_length=150)  # Guarda el título del post
    introduction = models.TextField()  # Guarda el texto de cabecera del post
    body = models.TextField()  # Guarda el texto del cuerpo del post
    url = models.URLField(blank=True, null=True, default="")  # Guarda la URL de la foto/video del post
    published_date = models.DateTimeField()  # Guarda la fecha de publicación del post
    created_at = models.DateTimeField(auto_now_add=True)  # Guarda la fecha de la creación del post
    modified_at = models.DateTimeField(auto_now=True)  # Guarda la fecha de última modificación del post

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
