from django.db import models

# Create your models here.
from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()  # Поле для даты релиза

    def __str__(self):
        return self.title
