from django.db import models

# Create your models here.
from django.db.models import FilePathField


class Describes(models.Model) :
    title = models.CharField(max_length=100)
    description = models.TextField()