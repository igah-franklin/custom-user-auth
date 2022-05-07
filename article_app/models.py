from ast import mod
from statistics import mode
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    def __str__(self) -> str:
        return f'owner: {self.owner} title: {self.title}'