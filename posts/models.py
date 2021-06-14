from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    title = models.CharField('タイトル', max_length=120)
    body = models.TextField('本文')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return f"[${self.author.username}] ${self.title}"