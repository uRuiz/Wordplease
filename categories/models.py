from django.db import models


class Category(models.Model):

    category_name = models.CharField(max_length=20)  # Guarda el nombre de la categoría

    def __str__(self):
        return self.category_name
