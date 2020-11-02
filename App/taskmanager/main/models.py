from django.db import models

# Create your models here.
from django.db.models import CharField


class Grade (models.Model):
    lesson: CharField = models.CharField(max_length=50)
